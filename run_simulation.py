# Run simulation
from schedules import Schedule

def simulation(stops_fyrktorget, stops_bockkranen, travel_time_fyrktorget, travel_time_bockkranen, depatures_fyrktorget, depatures_bockkranen):
    for depature_fyrktorget, depature_bockkranen in zip(depatures_fyrktorget, depatures_bockkranen):
        steps_fyrktorget = 60 // depature_fyrktorget
        steps_bockkranen = 60 // depature_bockkranen
        
        for i in range(60):
            pass

def main():
    bus_schedule = Schedule()
    stops_fyrktorget, stops_bockkranen, travel_time_fyrktorget, travel_time_bockkranen, depatures_fyrktorget, depatures_bockkranen = bus_schedule.get_schedule()
    simulation(stops_fyrktorget, stops_bockkranen, travel_time_fyrktorget, travel_time_bockkranen, depatures_fyrktorget, depatures_bockkranen)

if __name__ == '__main__':
    main()