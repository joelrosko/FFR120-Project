# Run simulation
import matplotlib.pyplot as plt
import numpy as np
import json

import initialize_stops
from simulation_window import Window
from bus import Bus

n_buses = 2
delay_time = []

def load_json():
    with open('data/travel_time.json', 'r') as json_file:
        tmp_travel_times = json.load(json_file)

    return tmp_travel_times['times']

def simulation(bstoplist, buses, window, travel_times):
    for t in range(10000):
        for bus_stop in bstoplist:
            bus_stop.create_passenger(t, travel_times)

        for bus_idx, current_bus in enumerate(buses):
            at_stop, stop_idx = current_bus.bus_at_stop()
            if at_stop:
                passenger_end_idx = [passenger.end_index for passenger in current_bus.passenger_list]
                if any(passenger_end_idx == stop_idx):
                    passenger_idx = np.where(passenger_end_idx == stop_idx)
                    delay_time.append(current_bus.passenger_list[passenger_idx[0][0]].delay_time())
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
    buses = [Bus(bstoplist, 0), Bus(bstoplist, 3.14)]
    for bus in buses:
        window.add_bus(bus.position)

    simulation(bstoplist, buses, window, travel_times)

if __name__ == '__main__':
    main()