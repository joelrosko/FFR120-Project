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
    times.insert(0,0)
    print(times)
    stoplist = []

    angle_1min = np.pi/(48)
    tmptime = 0
    for id, name in enumerate(names):
        tmptime += times[id]
        pos = angle_1min*tmptime
        stoplist.append(BusStop(name + " norrgående", pos, id))

    for id, name in enumerate(reversed(names)):
        tmptime += times[-id]
        pos = angle_1min * tmptime
        stoplist.append(BusStop(name + " södergående", pos, id+22))

    return stoplist


