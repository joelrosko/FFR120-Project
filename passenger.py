import numpy as np


class Passenger:
    def __init__(self, start_time, bus_stop_index):
        self.start_time = start_time
        self.waiting_time = []
        self.traveling_time = []
        self.start_index = bus_stop_index
        if self.start_index < 22:
            self.end_index = int(np.random.randint(self.start_index+1, 23, 1))
        else:
            self.end_index = int(np.random.randint(self.start_index + 1, 45, 1))

    def __repr__(self):
        return f'From bus stop "{self.start_index}" to "{self.end_index}"\n' \


    def get_times(self):
        return f'Start time: {self.start_time} ts\n' \
               f'Waiting time: {self.waiting_time} ts\n' \
               f'Travel time: {self.traveling_time} ts\n'

    def wait_time(self, current_time):
        self.waiting_time = current_time - self.start_time

    def travel_time(self, curr_time):
        self.traveling_time = curr_time - self.start_time
