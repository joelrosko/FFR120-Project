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
    print(times["times"])
    stoplist = []


    for id, name in enumerate(names):
        pos = id*np.pi
        stoplist.append(BusStop(name, pos, id))

    print(stoplist)

#initialize_stoplist()