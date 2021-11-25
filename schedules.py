import json

class Schedule:
    def __init__(self):
        self.set_stops()
        self.set_time_schedule()
        self.set_depatures()

    def set_stops(self):
        with open('data/stops.json', 'r') as json_file:
            self.stops = json.load(json_file)

    def set_travel_time(self):
        with open('data/travel_time.json', 'r') as json_file:
            self.travel_time = json.load(json_file)
    
    def set_depatures(self):
        with open('data/depatures.json', 'r') as json_file:
            self.depatures = json.load(json_file)
    
    def get_schedule(self):
        return self.stops, self.stops[::-1], self.travel_time['times'], self.travel_time['times'][::-1], self.depatures['Fyrktorget'], self.depatures['Bockkranen']