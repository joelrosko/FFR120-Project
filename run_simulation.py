# Run simulation
import matplotlib.pyplot as plt
import numpy as np

import initialize_stops
import simulation_window
import bus

n_buses = 2
delay_time = []

def simulation(bstoplist, buses, window):
    for t in range(1000):
        for bus_stop in bstoplist:
            bus_stop.create_passenger(t)

        for bus_idx, current_bus in enumerate(buses):
            at_stop, stop_idx = current_bus.bus_at_stop()
            if at_stop:
                if current_bus.passenger_list[:].end_index.any() == stop_idx:
                    passenger_idx = np.where(current_bus.passenger_list[:].end_index == stop_idx)
                    delay_time.append(current_bus.passenger_list[passenger_idx[0]].delay_time())
                    current_bus.remove_passenger(passenger_idx[0])
                elif bstoplist[stop_idx].waiting_list != []:
                    current_bus.add_passengers(t)
                else:
                    current_bus.boarding_complete()
            else:
                current_bus.move_bus()
                window.move_bus(bus_idx, current_bus.position)
        
        plt.pause(0.01)

def main():
    bstoplist = initialize_stops.initialize_stoplist()
    window = simulation_window(bstoplist)
    buses = [bus(bstoplist, 0), bus(bstoplist, 3.14)]

    simulation(bstoplist, buses, window)

if __name__ == '__main__':
    main()