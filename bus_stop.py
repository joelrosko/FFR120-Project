import json


def load_json():
    with open('data/stops.json', 'r') as json_file:
        params = json.load(json_file)

    return params.keys()


class BusStop:

    def __init__(self, name: str):
        self.name = name
        self.position = None
        self.waiting_list = []

    def __repr__(self):
        return f'Bus stop "{self.name}":\n Waiting: {self.waiting_list}\n'

    def add_passenger(self):
        # TODO should create a passenger instance at the stop.
        self.waiting_list.append("Testman") # Temporary testman string instead of Passenger


    def board_passenger(self):
        # TODO return a passenger to be boarded, maybe the one who waited the longest
        pass

    def add_time(self):
        # Adds +1 time spent att bus stop for all passengers
        # TODO check if it works with Passenger class
        for passenger in self.waiting_list:
            passenger.stop_time += 1


# Tests:
valand = BusStop("Valand")
print(valand)

hej = load_json()

stoplist = []
for key in hej:
    stoplist.append(BusStop(key))

for stop in stoplist:
    stop.add_passenger()

print(stoplist)