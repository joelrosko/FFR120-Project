import matplotlib.pyplot as plt
import json
import numpy as np
import pandas as pd
import matplotlib.dates as md
plt.style.use('seaborn')


def load_json(filename, field='delay_times'):
    with open(f'data/{filename}.json', 'r') as json_file:
        data = json.load(json_file)

    return data[field]


def get_timestamps(array):
    times = []
    for t in array[:, 1]:
        times.append(pd.Timestamp(t, unit='s'))
    return times


def delay_time():
    control1 = np.array(load_json('front/delay_times_front1'))
    for i in range(2,6):
        control1 = np.append(control1, load_json(f'front/delay_times_front{i}'), axis=0)
    df1 = pd.DataFrame({'delay': control1[:, 0]})
    df1.index = get_timestamps(control1)
    df1.sort_index(inplace=True)

    no_control = np.array(load_json('no_control/delay_times_no_control1'))
    for i in range(2,6):
        no_control = np.append(no_control, load_json(f'no_control/delay_times_no_control{i}'), axis=0)
    df_nc = pd.DataFrame({'delay': no_control[:, 0]})
    df_nc.index = get_timestamps(no_control)
    df_nc.sort_index(inplace=True)

    control2 = np.array(load_json('front_back/delay_times_front_back1'))
    for i in range(2,6):
        control2 = np.append(control2, load_json(f'front_back/delay_times_front_back{i}'), axis=0)
    df2 = pd.DataFrame({'delay': control2[:,0]})
    df2.index = get_timestamps(control2)
    df2.sort_index(inplace=True)

    scheduled = np.array(load_json('schedule/delay_times_schedule1'))
    for i in range(2,6):
        scheduled = np.append(scheduled, load_json(f'schedule/delay_times_schedule{i}'), axis=0)
    df3 = pd.DataFrame({'delay': scheduled[:,0]})
    df3.index = get_timestamps(scheduled)
    df3.sort_index(inplace=True)

    roll_nc = df_nc.rolling('600s', min_periods=1).mean()
    roll1 = df1.rolling('600s', min_periods=1).mean()
    roll2 = df2.rolling('600s', min_periods=1).mean()
    roll3 = df3.rolling('600s', min_periods=1).mean()

    fig = plt.figure("Passenger delays")
    ax_dt = fig.add_subplot()
    ax_dt.plot(roll_nc, linewidth=2, color='red', label='Uncontrolled')
    ax_dt.plot(roll1, linewidth=2, color='skyblue', label='Front control')
    ax_dt.plot(roll2, linewidth=2, color='g', label='Front and back control')
    ax_dt.plot(roll3, linewidth=2, color='y', label='Schedule based')
    ax_dt.set_title('Moving average passenger delay over 10 minutes')
    ax_dt.set_xlabel('Time [hours]')
    ax_dt.set_ylabel('Delay [s]')
    ax_dt.legend()
    ax_dt.xaxis.set_major_formatter(md.DateFormatter('%H'))


def waiting_time():
    # Not used
    data = load_json('waiting_times', 'waiting_times')
    moving_average = np.convolve(data, np.ones(500), 'valid') / 500
    plt.plot(np.linspace(0,8*3600, len(moving_average)), moving_average, linewidth=2, color='skyblue')


def bunching_coef():
    control = np.array(load_json('front/bunching_coef_front1', 'bunching_coef'))
    for i in range(2,6):
        control = np.add(control, np.array(load_json(f'front/bunching_coef_front{i}', 'bunching_coef')))
    control = control/5

    double_control = load_json('front_back/bunching_coef_front_back1', 'bunching_coef')
    for i in range(2,6):
        double_control = np.add(double_control, np.array(load_json(f'front_back/bunching_coef_front_back{i}', 'bunching_coef')))
    double_control = double_control/5

    no_control = load_json('no_control/bunching_coef_no_control1', 'bunching_coef')
    for i in range(2,6):
        no_control = np.add(no_control, np.array(load_json(f'no_control/bunching_coef_no_control{i}', 'bunching_coef')))
    no_control = no_control/5

    scheduled = load_json('schedule/bunching_coef_schedule1', 'bunching_coef')
    for i in range(2,6):
        scheduled = np.add(scheduled, np.array(load_json(f'schedule/bunching_coef_schedule{i}', 'bunching_coef')))
    scheduled = scheduled/5

    fig = plt.figure('Bunching levels')
    ax_b = fig.add_subplot()
    ax_b.plot(np.linspace(0, 8, len(control)), control, linewidth=2, color='skyblue', label='Front control')
    ax_b.plot(np.linspace(0, 8, len(double_control)), double_control, linewidth=2, color='g', label='Front and back control')
    ax_b.plot(np.linspace(0, 8, len(no_control)), no_control, linewidth=2, color='red', label='No control')
    ax_b.plot(np.linspace(0, 8, len(no_control)), scheduled, linewidth=2, color='y', label='Schedule based')
    ax_b.set_title('Bunching levels, sampled every 10 min')
    ax_b.set_xlabel('Time [h]')
    ax_b.set_ylabel('Variance in distances between buses')
    ax_b.legend()


def var_passengers():
    control = load_json('var_passengers_control', 'var_passengers')
    dubble_control = load_json('var_passengers_doublecontrol', 'var_passengers')
    no_control = load_json('no_control/var_passengers_nocontrol', 'var_passengers')
    fig = plt.figure('Passenger variance')
    ax_vp = fig.add_subplot()
    ax_vp.plot(np.linspace(0, 8, len(control)), control, linewidth=2, color='skyblue')
    ax_vp.plot(np.linspace(0, 8, len(dubble_control)), dubble_control, linewidth=2, color='g')
    ax_vp.plot(np.linspace(0, 8, len(no_control)), no_control, linewidth=2, color='r')
    ax_vp.set_xlabel('Time [h]')
    ax_vp.set_ylabel('Variance in passengers on buses')
    ax_vp.set_title('Passenger variance')
    ax_vp.legend()


def waiting_passengers():
    control = load_json('waiting_passengers_control', 'waiting_passengers')
    double_control = load_json('waiting_passengers_doublecontrol', 'waiting_passengers')
    no_control = load_json('waiting_passengers_nocontrol', 'waiting_passengers')
    fig = plt.figure("Waiting passengers")
    ax_wp = fig.add_subplot()
    ax_wp.plot(np.linspace(0,8, len(control)), control, linewidth=2, color='skyblue')
    ax_wp.plot(np.linspace(0,8, len(no_control)), no_control, linewidth=2, color='red')
    ax_wp.set_title('Passengers waiting at stops')
    ax_wp.set_ylabel('Number of passengers')
    ax_wp.set_xlabel('Time [h]')


def main():
    delay_time()
    bunching_coef()
    # waiting_passengers()
    # var_passengers()


if __name__ == '__main__':
    main()
    plt.show()