import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import numpy as np

class Window:
    def __init__(self, stops):
        self.fig, self.ax = plt.subplots(1,1, figsize=[6,6])
        self.x0 = 15
        self.y0 = 15
        self.r = 10
        self.stops = []
        self.stop_staple = []
        self.passenger_on_stop = np.zeros([1, len(stops)])
        self.buses = []
        self.window_style()
        self.x_pos = np.zeros([1, len(stops)])
        self.y_pos = np.zeros([1, len(stops)])
        self.x_angle = np.zeros([1, len(stops)])
        self.y_angle = np.zeros([1, len(stops)])
        self.init_window(stops)

    
    def window_style(self):
        self.ax.set_xlim(0,30)
        self.ax.set_ylim(0,30)
        self.ax.axis('off')
    
    def init_window(self, stops):
        circ = plt.Circle((15, 15), 10, color='grey', fill=False)
        self.ax.add_patch(circ)
        p = 0
        for beta in stops:
            x = self.x0 + self.r*np.cos(beta.position)
            y = self.y0 + self.r*np.sin(beta.position)
            self.x_angle[0, p] = np.cos(beta.position)
            self.y_angle[0, p] = np.sin(beta.position)
            self.x_pos[0, p] = x
            self.y_pos[0, p] = y
            self.stops.append(plt.Circle((x, y), 0.1, color='k', fill=True))
            self.stop_staple.append(ptc.FancyArrowPatch(posA=(x, y),
                                                        posB=(x+np.cos(beta.position), y+np.sin(beta.position))))
            self.ax.add_patch(self.stop_staple[-1])
            self.ax.add_patch(self.stops[-1])
            p += 1
        self.ax.set_title('0h 0min', color='w', backgroundcolor='k')
    
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
    
    def add_passengers(self, stop_idx, n_passengers):
        self.passenger_on_stop[0, stop_idx] = n_passengers

    def move_staple(self):
        for stop_index, nr_of_passengers in enumerate(self.passenger_on_stop[0, :]):
            self.stop_staple[stop_index].set_positions(posA=(self.x_pos[0, stop_index], self.y_pos[0, stop_index]),
                                                       posB=((self.x_pos[0, stop_index] -
                                                              0.1*nr_of_passengers*self.x_angle[0, stop_index]),
                                                       (self.y_pos[0, stop_index] -
                                                        0.1*nr_of_passengers*self.y_angle[0, stop_index])))

    def change_time(self, t):
        hours = np.floor(t/3600)
        minutes = np.floor((t-hours*3600)/60)
        self.ax.set_title(f'{int(hours)}h {int(minutes)}min', fontsize='xx-large')

    def change_color(self, free_seats, bus_idx):
        if free_seats == 0:
            self.buses[bus_idx].set_color('r')
        elif free_seats < 50:
            self.buses[bus_idx].set_color('orange')
        else:
            self.buses[bus_idx].set_color('b')
