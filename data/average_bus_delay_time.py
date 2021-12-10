import numpy as np

low = np.load('spawn_probabilities_low.npy')
#print(low, 'spawn/s', '\n\n', '{...}*60s*48min*2=[spawn/s*s/min*min/varv]=[spawn/varv]')
bus_travel_time = 39
low_sec = np.multiply(low, bus_travel_time*2*60)
bustime = 48
pick_up_time = bustime-bus_travel_time
tillagg_low = np.sum(low_sec)/600
varvtid = np.multiply(tillagg_low, 1/600)
print(np.sum(low_sec), 'antal passagerare/(buss och varv)', '->{...}*2s/20st*1/60s ->')
print(bustime, 'min ger att', pick_up_time*20/2*60, 'passagerare kan plockas upp')
print('På', bustime, 'min spawnar', np.multiply(np.sum(low), bustime*2*60), 'passagerare')
if pick_up_time*20/2*60 > np.multiply(np.sum(low), bustime*2*60):
    print('Ok!')
else:
    print('Not ok!')
# print(np.max(low)/np.min(low))
# print(len(low))
# new_low = np.multiply(low, 1/2.08)
# print(new_low)
# np.save('spawn_probabilities_low.npy', new_low)

