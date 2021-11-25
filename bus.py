class Bus:
    def __init__(self, start_pos, n_passengers):
        self.max_passenger = 100
        self.start_pos = start_pos
        self.n_passengers = n_passengers
    
    def set_position(self, pos):
        self.position = pos

    def get_position(self):
        return self.position
    
    def add_passengers(self):
        pass

    def lose_passengers(self):
        pass