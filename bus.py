import numpy as np
from initialize_stops import initialize_stoplist, load_json
from bus_stop import BusStop
import json




class Bus:

    def __init__(self, stops, start_pos, n_passengers=0):
        self.angular_velocity = 0.001315789473684   # 360/(38min*2*3600s) = 360/273600 {old = 0.001090277777777778}
        self.max_passengers = 100
        self.position = start_pos
        self.n_passengers = n_passengers
        self.passenger_list = []
        self.at_stop = False
        self.stops = stops
        self.stop_position = np.array([self.stops[i].position for i in range(len(self.stops))])
        self.next_stop = np.where(start_pos < self.stop_position)[0][0]
        self.previous_stop = self.next_stop - 1
        self.time_to_next_stop = 0
        self.times = load_json('data/travel_time.json')
        self.times = self.times["times"]
        self.times.extend(self.times[::-1])
        self.times = list(np.array(self.times)*60)
        self.late = False
        self.first_time = True

    def bus_at_stop(self):
        if (np.abs(self.stop_position[self.next_stop] - self.position)) <= self.angular_velocity:
            self.previous_stop = self.next_stop
            self.at_stop = True
        else:
            self.at_stop = False

        return self.at_stop, self.previous_stop

    def boarding_complete(self):
        self.at_stop = False
        self.next_stop += 1
        self.next_stop = self.next_stop % len(self.stop_position)

        self.time_to_next_stop += self.times[self.next_stop-1]


    def move_bus(self):
        if not self.at_stop:
            self.position += self.angular_velocity
            self.position = self.position % (2*np.pi)

    def move_bus_slow(self):
        self.position += self.angular_velocity/2
        self.position = self.position % (2*np.pi)

    def late_or_not(self, t):
        if t >= self.time_to_next_stop:
            self.late = True
        else:
            self.late = False

    def n_free_seats(self):
        return self.max_passengers - self.n_passengers
    
    def add_passenger(self, current_stop, t):
        if self.n_passengers < self.max_passengers:
            self.n_passengers += 1
            self.passenger_list.append(current_stop.board_passenger(t))
        else:
            self.boarding_complete()

    def remove_passenger(self, idx):
        if self.n_passengers > 0:
            self.n_passengers -= 1
            self.passenger_list.pop(idx)

    def __repr__(self):
        return f'At stop: {self.at_stop} pos: {self.position}: passengers: {self.n_passengers}\n previous stop: ' \
               f'{self.previous_stop} next stop: {self.next_stop}\n'
        # return self.passenger_list.pop(idx)



