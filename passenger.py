import json
import numpy as np


# def load_json():
#     with open('data/travel_time.json', 'r') as json_file:
#         params = json.load(json_file)
#
#     return params


class Passenger:
    def __init__(self, start_time, bus_stop_index, travel_times):
        self.start_time = start_time
        self.waiting_time = 0
        self.traveling_time = 0
        self.start_index = bus_stop_index
        if self.start_index < 21:
            self.end_index = int(np.random.randint(self.start_index + 1, 21, 1))
            self.estimated_time = np.sum(travel_times[self.start_index - 1:self.end_index - 1])
        else:
            self.end_index = int(np.random.randint(self.start_index, 42, 1))
            flipped_travel_times = travel_times[::-1]
            self.estimated_time = np.sum(flipped_travel_times[(self.start_index % 21)-1:(self.end_index % 21)-1])

    def __repr__(self):
        return f'From bus stop "{self.start_index}" to "{self.end_index}"\n' \


    def get_times(self):
        return f'Start time: {self.start_time} ts\n' \
               f'Waiting time: {self.waiting_time} ts\n' \
               f'Travel time: {self.traveling_time} ts\n'\
               f'Estimated time: {self.estimated_time} ts\n'

    def wait_time(self, current_time):
        self.waiting_time = current_time - self.start_time

    def travel_time(self, curr_time):
        self.traveling_time = curr_time - self.start_time

    def delay_time(self):
        return self.traveling_time - self.estimated_time


# hej = load_json()
# ki = hej["times"]
# p1 = Passenger(11, 1, ki)
# print(p1, p1.get_times())
