import matplotlib.pyplot as plt

class Window:
    def __init__(self, stops):
        self.fig, self.ax = plt.subplots(1,1)
        self.window_style(stops)
        self.buses = []
    
    def window_style(self):
        self.ax.set_xlim(0,30)
        self.ax.set_ylim(0,30)
        self.ax.axis('off')
    
    def init_window(self, stops):
        for (x, y) in stops:
            stop = plt.Circle((x, y), 0.1, color='k', fill=True)
            self.ax.add_patch(stop)
    
    def add_bus(self, start_pos):
        self.buses.append(plt.Rectangle(start_pos, 0.1, 0.5, color='b'))
        self.ax.add_patch(self.buses[-1])
    
    def move_bus(self, n_bus, beta, new_xy):
        self.buses[n_bus].set_angle(beta)
        self.buses[n_bus].set_xy(new_xy)