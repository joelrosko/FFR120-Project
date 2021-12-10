import matplotlib.pyplot as plt
plt.style.use('seaborn')
import json
import numpy as np

def load_json(filename, field):
    with open(f'data/{filename}.json', 'r') as json_file:
        data = json.load(json_file)

    return data[field]

def delay_time():
    data = load_json('delay_times', 'delay_times')
    moving_average = np.convolve(data, np.ones(500), 'valid') / 500
    plt.plot(np.linspace(0,8*3600, len(moving_average)), moving_average, linewidth=2, color='skyblue')

def waiting_time():
    data = load_json('waiting_times', 'waiting_times')
    moving_average = np.convolve(data, np.ones(500), 'valid') / 500
    plt.plot(np.linspace(0,8*3600, len(moving_average)), moving_average, linewidth=2, color='skyblue')

def bunching_coef():
    data = load_json('bunching_coef', 'bunching_coef')
    plt.plot(np.linspace(0,8*3600, len(data)), data, linewidth=2, color='skyblue')

def var_passengers():
    data = load_json('var_passengers', 'var_passengers')
    plt.plot(np.linspace(0,8*3600, len(data)), data, linewidth=2, color='skyblue')

def waiting_passengers():
    data = load_json('waiting_passengers', 'waiting_passengers')
    plt.plot(np.linspace(0,8*3600, len(data)), data, linewidth=2, color='skyblue')

def main():
    waiting_passengers()

if __name__ == '__main__':
    main()
    plt.show()