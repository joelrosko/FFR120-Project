# Run simulation
import matplotlib.pyplot as plt
import initialize_stops
import simulation_window
import bus

n_buses = 2


def simulation(bstoplist, buses, window):
    for t in range(1000):
        for bus_stop in bstoplist:
            bus_stop.create_passenger(t)

        for bus_idx, current_bus in enumerate(buses):
            at_stop = current_bus.bus_at_stop()
            if at_stop:
                current_bus.passenger_list
                pass
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