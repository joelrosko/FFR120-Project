import matplotlib.pyplot as plt
plt.style.use('seaborn')
import json
import numpy as np
import pandas as pd
import matplotlib.dates as md
plt.style.use('seaborn')


def load_json(filename, field):
    with open(f'data/{filename}.json', 'r') as json_file:
        data = json.load(json_file)

    return data[field]


def get_timestamps(array):
    times = []
    for t in array[:, 1]:
        times.append(pd.Timestamp(t, unit='s'))
    return times


def delay_time():
    d_array = np.array(load_json('delay_times', 'delay_times'))
    df = pd.DataFrame({'delay': d_array[:, 0]})
    times = get_timestamps(d_array)
    df.index = times

    no_control = np.array(load_json('delay_times_nocontrol', 'delay_times'))
    df_nc = pd.DataFrame({'delay': no_control[:, 0]})
    df_nc.index = get_timestamps(no_control)

    roll = df.rolling('600s', min_periods=1).mean()
    roll_nc = df_nc.rolling('600s', min_periods=1).mean()

    fig = plt.figure("Passenger delays")
    ax_dt = fig.add_subplot()
    ax_dt.plot(roll, linewidth=2, color='skyblue', label='Controlled, how?')
    ax_dt.plot(roll_nc, linewidth=2, color='red', label='Uncontrolled')
    ax_dt.set_title('Moving average passenger delay over 10 minutes')
    ax_dt.set_xlabel('Time [hours]')
    ax_dt.set_ylabel('Delay [s]')
    ax_dt.legend()
    ax_dt.xaxis.set_major_formatter(md.DateFormatter('%H'))

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
    fig = plt.figure("Waiting passengers")
    ax_wp = fig.add_subplot()
    ax_wp.plot(np.linspace(0,8*3600, len(control))/60, control, linewidth=2, color='skyblue')
    ax_wp.plot(np.linspace(0,8*3600, len(no_control))/60, no_control, linewidth=2, color='red')
    ax_wp.set_title('Passengers waiting at stops')
    ax_wp.set_ylabel('Number of passengers')
    ax_wp.set_xlabel('Time [min]')


def main():
    waiting_passengers()
    delay_time()


if __name__ == '__main__':
    main()
    plt.show()