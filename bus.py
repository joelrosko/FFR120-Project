class Bus:
    def __init__(self, start_pos, n_passengers):
        self.max_passenger = 100
        self.start_pos = start_pos
        self.n_passengers = n_passengers
    
    def set_position(self, pos):
        self.position = pos

    def get_position(self):
        return self.position
    
    def add_passengers(self, n_add):
        if self.n_passengers < self.max_passenger:
            self.n_passengers += n_add

    def lose_passengers(self, n_remove):
        if self.n_passengers > 0:
            self.n_passengers -= n_remove

