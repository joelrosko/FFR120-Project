# Run simulation
import initialize_stops
import simulation_window
import bus

n_buses = 2


def simulation(bstoplist, buses, window):
    for t in range(1000):
        for bus_stop in bstoplist:
            pass
        
        for current_bus in buses:
            pass

def main():
    bstoplist = initialize_stops.initialize_stoplist()
    window = simulation_window(bstoplist)
    buses = [bus(bstoplist, 0), bus(bstoplist, 3.14)]

    simulation(bstoplist, buses, window)

if __name__ == '__main__':
    main()