from geopy.geocoders import Nominatim
import json


def load_json():
    with open('data/stop-names.json', 'r') as json_file:
        params = json.load(json_file)

    return params['stopNames']


def get_lat_lon(names):
    coords = {name:[] for name in names}
    geolocator = Nominatim(user_agent="bus-stops")
    for name in names:
        try:
            location = geolocator.geocode(name)
            coords[name] = [location.latitude, location.longitude]
            print((location.latitude, location.longitude))
        except:
            print('###########################################')
            print(f'location for {name} not found..')
            print('###########################################')
    
    return coords

def save_json(coords):
    with open('data/stops.json', 'w', encoding='utf-8') as json_file:
        json.dump(coords, json_file, ensure_ascii=False, indent=4)

def main():
    stop_names = load_json()
    coords = get_lat_lon(stop_names)
    save_json(coords)

if __name__ == "__main__":
    main()