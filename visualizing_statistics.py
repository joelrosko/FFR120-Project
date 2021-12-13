import matplotlib.pyplot as plt
plt.style.use('seaborn')
import json
import numpy as np

def load_json(filename, field):
    with open(f'data/{filename}.json', 'r') as json_file:
        data = json.load(json_file)

    return data[field]

def create_fig(title):
    fig, ax = plt.subplots(1,1)
    fig.suptitle(title)
    return fig, ax

def delay_time():
    data = load_json('delay_times', 'delay_times')
    moving_average = np.convolve(data, np.ones(500), 'valid') / 500
    plt.plot(np.linspace(0,8*3600, len(moving_average)), moving_average, linewidth=2, color='skyblue')

def waiting_time():
    data = load_json('waiting_times', 'waiting_times')
    moving_average = np.convolve(data, np.ones(500), 'valid') / 500
    plt.plot(np.linspace(0,8*3600, len(moving_average)), moving_average, linewidth=2, color='skyblue')

def bunching_coef():
    control = load_json('bunching_coef_control', 'bunching_coef')
    dubble_control = load_json('bunching_coef_dubblecontrol', 'bunching_coef')
    no_control = load_json('bunching_coef_nocontrol', 'bunching_coef')
    plt.plot(np.linspace(0,8*3600, len(control)), control, linewidth=2, color='skyblue')
    plt.plot(np.linspace(0,8*3600, len(dubble_control)), dubble_control, linewidth=2, color='g')
    plt.plot(np.linspace(0,8*3600, len(no_control)), no_control, linewidth=2, color='red')

def var_passengers():
    control = load_json('var_passengers_control', 'var_passengers')
    dubble_control = load_json('var_passengers_dubblecontrol', 'var_passengers')
    no_control = load_json('var_passengers_nocontrol', 'var_passengers')
    plt.plot(np.linspace(0,8*3600, len(control)), control, linewidth=2, color='skyblue')
    plt.plot(np.linspace(0,8*3600, len(dubble_control)), dubble_control, linewidth=2, color='g')
    plt.plot(np.linspace(0,8*3600, len(no_control)), no_control, linewidth=2, color='r')

def waiting_passengers():
    control = load_json('waiting_passengers_control', 'waiting_passengers')
    dubble_control = load_json('waiting_passengers_dubblecontrol', 'waiting_passengers')
    no_control = load_json('waiting_passengers_nocontrol', 'waiting_passengers')
    plt.plot(np.linspace(0,8*3600, len(control)), control, linewidth=2, color='skyblue')
    plt.plot(np.linspace(0,8*3600, len(dubble_control)), dubble_control, linewidth=2, color='g')
    plt.plot(np.linspace(0,8*3600, len(no_control)), no_control, linewidth=2, color='red')

def main():
    var_passengers()

if __name__ == '__main__':
    main()
    plt.show()