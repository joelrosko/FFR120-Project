import json

class Schedule:
    def __init__(self) -> None:
        self.set_stops()
        self.set_time_schedule()

    def set_stops(self):
        with open('data/stops.json', 'r') as json_file:
            self.stops = json.load(json_file)

    def set_time_schedule(self):
        with open('data/stops.json', 'r') as json_file:
            self.time_schedule = json.load(json_file)