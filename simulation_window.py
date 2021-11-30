import matplotlib.pyplot as plt
import numpy as np

class Window:
    def __init__(self, stops):
        self.fig, self.ax = plt.subplots(1,1)
        self.x0 = 15
        self.y0 = 15
        self.r = 10
        self.buses = []
        self.window_style(stops)
    
    def window_style(self):
        self.ax.set_xlim(0,30)
        self.ax.set_ylim(0,30)
        self.ax.axis('off')
    
    def init_window(self, stops):
        for beta in stops:
            x = self.x0 + self.r*np.cos(beta)
            y = self.y0 + self.r*np.sin(beta)
            stop = plt.Circle((x, y), 0.1, color='k', fill=True)
            self.ax.add_patch(stop)
    
    def add_bus(self, start_angle):
        x = self.x0 + self.r*np.cos(start_angle)
        y = self.y0 + self.r*np.sin(start_angle)
        self.buses.append(plt.Rectangle((x, y), 0.1, 0.5, start_angle*180/np.pi, color='b'))
        self.ax.add_patch(self.buses[-1])
    
    def move_bus(self, n_bus, new_angle):
        x = self.x0 + self.r*np.cos(new_angle)
        y = self.y0 + self.r*np.sin(new_angle)
        self.buses[n_bus].set_angle(new_angle*180/np.pi)
        self.buses[n_bus].set_xy((x, y))