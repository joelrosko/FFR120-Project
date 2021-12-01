# Run simulation
import matplotlib.pyplot as plt
import numpy as np
import json

import initialize_stops
from simulation_window import Window
from bus import Bus

n_buses = 20
delay_time = []

def load_json():
    with open('data/travel_time.json', 'r') as json_file:
        tmp_travel_times = json.load(json_file)

    return tmp_travel_times['times']

def simulation(bstoplist, buses, window, travel_times):
    for t in range(10000):
        print(f'At time step {t}')
        for n_stop, bus_stop in enumerate(bstoplist):
            bus_stop.create_passenger(t, travel_times)
            window.add_passengers(n_stop, len(bus_stop.waiting_list))

        for bus_idx, current_bus in enumerate(buses):
            at_stop, stop_idx = current_bus.bus_at_stop()
            if at_stop:
                passenger_end_idx = [passenger.end_index for passenger in current_bus.passenger_list]
                if any(passenger_end_idx == stop_idx):
                    passenger_idx = np.where(passenger_end_idx == stop_idx)
                    delay_time.append(current_bus.passenger_list[passenger_idx[0][0]].delay_time(t))
                    current_bus.remove_passenger(passenger_idx[0][0])
                elif bstoplist[stop_idx].waiting_list != []:
                    current_bus.add_passenger(bstoplist[stop_idx], t)
                else:
                    current_bus.boarding_complete()
            else:
                current_bus.move_bus()
                window.move_bus(bus_idx, current_bus.position)
        
        plt.pause(0.001)

def main():
    travel_times = load_json()
    bstoplist = initialize_stops.initialize_stoplist()
    window = Window(bstoplist)
    buses = []
    bus_pos = np.linspace(0, 2*np.pi, n_buses, endpoint=False)
    for pos in bus_pos:
        buses.append(Bus(bstoplist, pos))

    for bus in buses:
        window.add_bus(bus.position)

    simulation(bstoplist, buses, window, travel_times)
    mean_delay_time = np.mean(delay_time)
    print(f'Average delay time {mean_delay_time/60} min')

if __name__ == '__main__':
    main()