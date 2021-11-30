from bus_stop import BusStop
import json
import numpy as np


def load_json(name):
    with open(name, 'r') as json_file:
        params = json.load(json_file)

    return params


def initialize_stoplist():
    names = load_json('data/stops.json').keys()
    times = load_json('data/travel_time.json')
    times = times["times"]
    times.insert(0, 0)

    stop_list = []
    angle_1min = np.pi/48
    tmptime = 0

    for id1, name in enumerate(names):
        tmptime += times[id1]
        pos = angle_1min*tmptime
        stop_list.append(BusStop(f"{name} norrgående", pos, id1))

    for id2, name in enumerate(reversed(names)):
        tmptime += times[-id2]
        pos = angle_1min * tmptime
        stop_list.append(BusStop(f"{name} södergående", pos, id2 + 22))

    return stop_list


