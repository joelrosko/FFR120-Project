import numpy as np


class Bus:
    def __init__(self, bus_stops, start_pos, n_passengers=0):
        self.angular_velocity = 0.001090277777777778
        self.max_passengers = 10
        self.position = start_pos
        self.n_passengers = n_passengers
        self.at_stop = False
        self.bus_stops = bus_stops
        self.next_stop = np.where(start_pos < self.bus_stops)[0][0]  # change


    def bus_at_stop(self):
        if (self.bus_stops[self.next_stop] - self.position) < self.angular_velocity:
            self.at_stop = True
            self.next_stop += 1
        else:
            self.at_stop = False

    def move_bus(self):
        self.bus_at_stop()
        if not self.at_stop:
            self.position += self.angular_velocity

    def n_free_seats(self):
        return self.max_passengers - self.n_passengers
    
    def add_passengers(self):
        if self.n_passengers < self.max_passengers:
            self.n_passengers += 1

    def remove_passengers(self):
        if self.n_passengers > 0:
            self.n_passengers -= 1

    #def get_nr


if __name__ == '__main__':

    # bus1 = Bus(1, 5)
    # for i in range(100):
    #     bus1.add_passengers()
    #     print(bus1.n_free_seats())
    #     print(bus1.n_passengers)
    #     bus1.remove_passengers()
    #
    # print(bus1.n_passengers)
    # print(bus1.at_stop)
    BUSSTOPS = np.array([0, 0.06544985, 0.39269908, 0.65449847, 0.85084801,
       0.91629786, 0.9817477 , 1.1126474 , 1.24354709, 1.30899694,
       1.50534648, 1.63624617, 1.89804556, 2.0943951 , 2.15984495,
       2.29074464, 2.35619449, 2.55254403, 2.74889357, 2.81434342,
       2.94524311, 3.14159265])

    start_pos = (np.pi*np.random.randint(180))/180

    # b1 = 0.0
    # b2 = 0.06545
    bus1 = Bus(BUSSTOPS, start_pos, 5)
    # bus1.move_bus()
    print(bus1.next_stop)
    print(bus1.position)
    # i = 0
    # while True:
    #
    #     bus1.move_bus()
    #     print(bus1.position)
    #     if (BUSSTOPS[i] - bus1.position) < 0.001090277777777778:
    #         i += 1
    #         print('at stop')
    #
    #
    #
    #
    #
    #
