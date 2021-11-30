class BusStop:

    def __init__(self, name: str):
        self.name = name
        self.waiting_list = []

    def __repr__(self):
        return f'Bus stop "{self.name}":\n Waiting: {self.waiting_list}'

    def add_passenger(self):
        # TODO should create a passenger at the stop.
        pass

    def board_passenger(self):
        # TODO return a passenger to be boarded, maybe the one who waited the longest
        pass

    def add_time(self):
        # Adds +1 time spent att bus stop for all passengers
        # TODO check if it works with Passenger class
        for passenger in self.waiting_list:
            passenger.stop_time += 1


# Tests:
valand = BusStop("Valand")
print(valand)
