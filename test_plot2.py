import matplotlib.pyplot as plt
import json
import numpy as np

def load_json():
    with open('data/travel_time.json', 'r') as json_file:
        params = json.load(json_file)

    return params

def pr_step(travel_time):
    tot_time = sum(travel_time['times'])
    pr_steps = []
    for time in travel_time['times']:
        pr_steps.append(time/tot_time)
    
    return pr_steps

def pos_stops(pr_steps, r=10, x0=15, y0=15):
    pos = []
    for i in range(len(pr_steps)+1):
        beta = sum(pr_steps[:i])*np.pi
        pos.append([x0 + r*np.cos(beta), y0 + r*np.sin(beta)])
    
    return pos

def pos_stops2(pr_steps, r=10, x0=15, y0=15):
    pos = []
    for i in range(len(pr_steps)+1):
        beta = sum(pr_steps[:i])*(-np.pi)
        pos.append([x0 + r*np.cos(beta), y0 + r*np.sin(beta)])
    
    return pos

travel_time = load_json()
pr_steps = pr_step(travel_time)
stop_pos = pos_stops(pr_steps)
stop_pos2 = pos_stops2(pr_steps)

circ_o = np.pi * 8

fig, ax = plt.subplots(1,1)
fig.show()
fig.suptitle('Bus')
#ax = plt.gca()
circ = plt.Circle((15, 15), 10, color='grey', fill=False)
#start = plt.Circle((5, 1), 0.2, color='b', fill=True)
#end = plt.Circle((5, 9), 0.2, color='b', fill=True)
ax.add_patch(circ)
for (x,y) in stop_pos:
    stop = plt.Circle((x, y), 0.1, color='k', fill=True)
    ax.add_patch(stop)

for (x,y) in stop_pos2:
    stop = plt.Circle((x, y), 0.1, color='k', fill=True)
    ax.add_patch(stop)

stop._set_facecolor('g')    # Change color of existing stop
stop._set_edgecolor('g')

# Plot bus
bus = plt.Rectangle((25+0.1, 15-0.15), 0.2, 0.5, color='b')
ax.add_patch(bus)

ax.set_xlim(0,30)
ax.set_ylim(0,30)
ax.axis('off')
'''
for i, (x,y) in enumerate(stop_pos):
    beta = sum(pr_steps[:i])*180
    bus.set_angle(beta)
    bus.set_xy((x,y))
    plt.pause(1)
'''
beta = 0
omega = np.pi/(48*60)
x0 = 15
y0 = 15
x = 25
y = 15
r = 10
for minutes in range(1,48*10):
    for secondes in range(60):
        beta += omega
        x = x0 + r*np.cos(beta)
        y = y0 + r*np.sin(beta)
        bus.set_angle(beta*180/np.pi)
        bus.set_xy((x,y))
        plt.pause(0.0001)
#plt.savefig('figures/first_circle_plot.png')
plt.show()