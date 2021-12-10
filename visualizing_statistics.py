import matplotlib.pyplot as plt
plt.style.use('seaborn')
import json

def load_json(filename, field):
    with open(f'data/{filename}.json', 'r') as json_file:
        data = json.load(json_file)

    return data[field]

def delay_time():
    data = load_json('delay_times', 'delay_times')
    

def main():
    pass

if __name__ == '__main__':
    main()