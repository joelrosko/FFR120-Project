import matplotlib.pyplot as plt

class Window:
    def __init__(self, stop_coords):
        self.fig, self.ax = plt.subplots(1,1)
        self.ax.plot(stop_coords, '.-')