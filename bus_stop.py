import json
import passenger
import numpy as np


def load_json():
    with open('data/stops.json', 'r') as json_file:
        params = json.load(json_file)

    return params


class BusStop:

    def __init__(self, name: str, position, index):
        self.name = name
        self.position = position
        self.waiting_list = []
        self.index = index

    def __repr__(self):
        return f'Bus stop [{self.index}] "{self.name}" at pos: {self.position}:\n Waiting: {self.waiting_list}\n'

    def add_passenger(self, current_time):
        # TODO should create a passenger instance at the stop. (time of arrival)
        self.waiting_list.append(passenger.Passenger(current_time, self.index))  # Temporary testman string instead of Passenger

    def board_passenger(self, current_time):
        # TODO return a passenger to be boarded, maybe the one who waited the longest

        if len(self.waiting_list) > 0:
            self.waiting_list[0].wait_time(current_time)    # Calls Passenger.wait_time() to measure time spent at stop
            return self.waiting_list.pop(0)
        else:
            print("Empty waiting list?")


# Tests:
# valand = BusStop("Valand", np.pi/2, 1337)
# print(valand)
#
# hej = load_json()
#
# stoplist = []
# for id, key in enumerate(hej.keys()):
#     stoplist.append(BusStop(key, id*np.pi/(30), id))
#
# for bstop in stoplist:
#     bstop.add_passenger(1)
#     bstop.add_passenger(2)
#
# print(stoplist)
#
# bus = []
# for id, bstop in enumerate(stoplist):
#     bus.append(bstop.board_passenger(id))
#
#
# print(stoplist)
# print(bus)
