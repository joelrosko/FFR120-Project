import numpy as np

w_time = 20
t_time = 40


class Passenger:
    def __init__(self, start_time):
        self.start_time = start_time
        self.waiting_time = []
        self.traveling_time = []
        self.start_pos = np.random.randint(1, 44, 1)
        if self.start_pos < 22:
            self.end_pos = np.random.randint(self.start_pos, 23, 1)
        else:
            self.end_pos = np.random.randint(self.start_pos+1, 45, 1)

    def __repr__(self):
        return f'From bus stop "{self.start_pos[0]}" to "{self.end_pos[0]}"\n' \
               f'Start time: {self.start_time} ts\n' \
               f'Waiting time: {self.waiting_time} ts\n' \
               f'Travel time: {self.traveling_time} ts\n'

    def wait_time(self, current_time):
        self.waiting_time = current_time - self.start_time

    def travel_time(self, curr_time):
        self.traveling_time = curr_time - self.start_time


p1 = Passenger(14)
print('Passenger arrived to bus stop:\n\n', p1)
p1.wait_time(w_time)
print('Bus picked passenger up:\n\n', p1)
p1.travel_time(t_time)
print('Passenger arrived to destination:\n\n', p1)
