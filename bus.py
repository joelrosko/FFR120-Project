import numpy as np
from initialize_stops import initialize_stoplist
from bus_stop import BusStop


class Bus:
    # STOP_POSITIONS = np.array([0.0, 0.06544985, 0.39269908, 0.65449847, 0.85084801, 0.91629786, 0.9817477, 1.1126474, 1.24354709, 1.30899694, 1.50534648, 1.63624617, 1.89804556, 2.0943951, 2.15984495, 2.29074464, 2.35619449, 2.55254403, 2.74889357, 2.81434342, 2.94524311, 3.14159265, 3.27249235, 3.33794219, 3.53429174, 3.73064128, 3.79609112, 3.92699082, 3.99244066, 4.1887902, 4.45058959, 4.58148929, 4.77783883, 4.84328867, 4.97418837, 5.10508806, 5.17053791, 5.23598776, 5.4323373, 5.69413668, 6.02138592, 6.08683577])

    def __init__(self, stops, start_pos, n_passengers=0):
        self.angular_velocity = 0.001090277777777778
        self.max_passengers = 100
        self.position = start_pos
        self.n_passengers = n_passengers
        self.passenger_list = []
        self.at_stop = False
        self.stops = stops
        self.stop_position = np.array([self.stops[i].position for i in range(len(self.stops))])
        self.next_stop = np.where(start_pos < self.stop_position)[0][0]
        self.previous_stop = 0

    def bus_at_stop(self):
        if (np.abs(self.stop_position[self.next_stop] - self.position)) < (self.angular_velocity/2):
            self.previous_stop = self.next_stop
            self.at_stop = True
        else:
            self.at_stop = False

        return self.at_stop, self.previous_stop

    def boarding_complete(self):
        self.at_stop = False
        self.next_stop += 1
        self.next_stop = self.next_stop % len(self.stop_position)

    def move_bus(self):
        self.bus_at_stop()
        if not self.at_stop:
            self.position += self.angular_velocity

    def n_free_seats(self):
        return self.max_passengers - self.n_passengers
    
    def add_passenger(self, current_stop, t):
        if self.n_passengers < self.max_passengers:
            self.n_passengers += 1
            self.passenger_list.append(current_stop.board_passenger(t))
        # passenger_list.append(BusStop.

    def remove_passenger(self, idx):
        if self.n_passengers > 0:
            self.n_passengers -= 1
            self.passenger_list.pop(idx)

        # return self.passenger_list.pop(idx)
    #def get_nr


if __name__ == '__main__':

    print('hej')
    # stops = initialize_stoplist()
    # # BS_positions = [stops[i].position for i in range(len(stops))]
    # bus1 = Bus(stops, 1, 5)

    # for i in range(100):
    #     bus1.add_passengers()
    #     print(bus1.n_free_seats())
    #     print(bus1.n_passengers)
    #     bus1.remove_passengers()
    #
    # print(bus1.n_passengers)
    # print(bus1.at_stop)
    # BUSSTOPS = np.array([0, 0.06544985, 0.39269908, 0.65449847, 0.85084801,
    #    0.91629786, 0.9817477 , 1.1126474 , 1.24354709, 1.30899694,
    #    1.50534648, 1.63624617, 1.89804556, 2.0943951 , 2.15984495,
    #    2.29074464, 2.35619449, 2.55254403, 2.74889357, 2.81434342,
    #    2.94524311, 3.14159265])
    #
    # start_pos = (np.pi*np.random.randint(360))/180
    # print(start_pos)
    # # b1 = 0.0
    # # b2 = 0.06545
    # bus1 = Bus(start_pos, 5)
    # # bus1.move_bus()
    # # print(bus1.next_stop)
    # # print(bus1.position)
    # i = 0
    # while True:
    #     print(bus1.position)
    #     bus1.move_bus()
    #     print(bus1.position)
        # if (BUSSTOPS[i] - bus1.position) < 0.001090277777777778:
    #         i += 1
    #         print('at stop')

    #
    #
    #
    #
