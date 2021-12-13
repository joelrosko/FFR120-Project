# Run simulation
import matplotlib.pyplot as plt
import numpy as np
import json
import math

import initialize_stops
from simulation_window import Window
from bus import Bus

n_runs = 10
n_buses = 20
delay_time = []
waiting_time = []
bunching_coef = []  # Variance in distance between buses
var_buss_passengers = []
n_waiting_passengers = []


def dist(b1,b2):
    return np.abs(math.atan2(np.sin(b1-b2), np.cos(b1-b2)))


def load_json():
    with open('data/travel_time.json', 'r') as json_file:
        tmp_travel_times = json.load(json_file)

    return tmp_travel_times['times']

def write_json(i):
    delay_time_dict = {'delay_times': delay_time}
    waiting_time_dict = {'waiting_times': waiting_time}
    bunching_coef_dict = {'bunching_coef': bunching_coef}
    var_buss_passengers_dict = {'var_passengers': var_buss_passengers}
    n_waiting_passengers_dict = {'waiting_passengers': n_waiting_passengers}
    with open(f'data/no_control/delay_times_nocontrol{i}.json', 'w', encoding='utf-8') as json_file:
        json.dump(delay_time_dict, json_file, ensure_ascii=False, indent=4)
    with open(f'data/no_control/waiting_times_nocontrol{i}.json', 'w', encoding='utf-8') as json_file:
        json.dump(waiting_time_dict, json_file, ensure_ascii=False, indent=4)
    with open(f'data/no_control/bunching_coef_nocontrol{i}.json', 'w', encoding='utf-8') as json_file:
        json.dump(bunching_coef_dict, json_file, ensure_ascii=False, indent=4)
    with open(f'data/no_control/var_passengers_nocontrol{i}.json', 'w', encoding='utf-8') as json_file:
        json.dump(var_buss_passengers_dict, json_file, ensure_ascii=False, indent=4)
    with open(f'data/no_control/waiting_passengers_nocontrol{i}.json', 'w', encoding='utf-8') as json_file:
        json.dump(n_waiting_passengers_dict, json_file, ensure_ascii=False, indent=4)


def get_var_passenger(buses):
    n_passengers = [bus.n_passengers for bus in buses]
    return np.var(n_passengers)


def get_waiting_passenger(bstoplist):
    waiting_passengers = [len(stop.waiting_list) for stop in bstoplist]
    return sum(waiting_passengers)


def get_bunching_coef(buses):
    dist = []
    for i, bus in enumerate(buses):
        b1 = bus.position
        b2 = buses[(i+1) % n_buses].position
        dist.append(math.atan2(np.sin(b1-b2), np.cos(b1-b2)))
    return np.var(dist)


def simulation(bstoplist, buses, window, travel_times, control):
    for t in range(8*3600):
        if t % 600 == 0 and t != 0:
            var_buss_passengers.append(get_var_passenger(buses))
            n_waiting_passengers.append(get_waiting_passenger(bstoplist))
            bunching_coef.append(get_bunching_coef(buses))
        if t % 1800 == 0 and t != 0:
            people_waiting = [len(bstop.waiting_list) for bstop in bstoplist]
            print(f'At time step {t}, {t/3600} hours')
            print(f'Average passenger delay: {np.average(np.array(delay_time)[:,0])/60} min')
            print(f'Standard deviation: {np.std(np.array(delay_time)[:,0])/60} min')
            print(f'Max {np.max(np.array(delay_time)[:,0])/60}, min {np.min(np.array(delay_time)[:,0])/60}')
            # print(f'Delays: {np.array(delay_time)[:,0]/60}')
            print(f'People waiting: {people_waiting}')
        for n_stop, bus_stop in enumerate(bstoplist):
            bus_stop.create_passenger(t, travel_times)
            window.add_passengers(n_stop, len(bus_stop.waiting_list))

        for bus_idx, current_bus in enumerate(buses):


            at_stop, stop_idx = current_bus.bus_at_stop()
            if at_stop:
                passenger_end_idx = [passenger.end_index for passenger in current_bus.passenger_list]
                if any(passenger_end_idx == stop_idx):
                    passenger_idx = np.where(passenger_end_idx == stop_idx)[0][0]
                    delay_time.append([int(current_bus.passenger_list[passenger_idx].delay_time(t)), t])
                    current_bus.remove_passenger(passenger_idx)
                elif bstoplist[stop_idx].waiting_list != []:
                    waiting_time.append([int(bstoplist[stop_idx].waiting_list[0].wait_time(t)), t])
                    current_bus.add_passenger(bstoplist[stop_idx], t)
                else:

                    # dist_infront = dist(current_bus.position, buses[(bus_idx + 1) % n_buses].position)
                    # dist_behind = dist(current_bus.position, buses[bus_idx - 1].position)
                    # if (dist_infront <= ((2*np.pi)/n_buses)*0.75) and control:
                    #     pass
                    # else:
                    #     current_bus.boarding_complete()

                    # if dist_infront < dist_behind and control:
                    #     pass
                    # else:
                    #     current_bus.boarding_complete()

                    current_bus.late_or_not(t)
                    if current_bus.late:
                        if current_bus.first_time:
                            current_bus.time_to_next_stop += t
                            current_bus.first_time = False
                        current_bus.boarding_complete()
                    else:
                        pass

            else:
                current_bus.move_bus()
                window.move_bus(bus_idx, current_bus.position)
                window.move_staple()

        plt.pause(0.001)


def main():
    for run in range(1, n_runs+1):
        travel_times = load_json()
        bstoplist = initialize_stops.initialize_stoplist()
        window = Window(bstoplist)
        buses = []
        bus_pos = np.linspace(0, 2*np.pi, n_buses, endpoint=False)
        for pos in bus_pos:
            buses.append(Bus(bstoplist, pos))

        for bus in buses:
            window.add_bus(bus.position)

        simulation(bstoplist, buses, window, travel_times, control=False)
        write_json(run)

if __name__ == '__main__':
    main()