# this file calls the API to get the blue bike details
import requests
from config import MAPBOX_TOKEN
import json
import urllib.parse
from math import radians, cos, sin, asin, sqrt
import math
import geopy.distance

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
STATION_DETAILS_URL = "https://gbfs.bluebikes.com/gbfs/en/station_status.json" 
STATION_INFO_URL = "https://gbfs.bluebikes.com/gbfs/en/station_information.json"

# get station status - no. of avail bikes, active or inactive  
def get_station_status(stat_id):
    response = requests.get(STATION_DETAILS_URL).json()
    stations_array = response['data']['stations']
    for station in stations_array:
        if station['station_id'] == stat_id :
            return station
    return("Station does not exist")


# returns formatted reply of the location of station, station status (Active/inactive) and number of avail bikes
def get_station_information(stat_id):
    station_info = get_station_status(stat_id)
    status = station_info['station_status']
    num_avail_bikes = station_info['num_bikes_available']
    
    response = requests.get(STATION_INFO_URL).json()
    stations_array = response['data']['stations']
    for station in stations_array:
        if station['station_id'] == stat_id :
            station_name = station['name']


    return (f"This station at {station_name} is {status} and has {num_avail_bikes} available bikes")

def get_avail_bikes(stat_id):
    station_info = get_station_status(stat_id)
    num_avail_bikes = station_info['num_bikes_available']
    return num_avail_bikes

# returns in form of list : [long, lat] 
def get_user_lat_long(place_name: str):
    query = urllib.parse.quote_plus(place_name, encoding=None, errors=None)
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    json_output = get_json(url)
    if(json_output['features']):
        return json_output['features'][0]['geometry']['coordinates']
    else:
        return("Address entered does not exist")
    
def calculate_distance(coords_1, coords_2):
    """
    this function makes use of the existing library : geopy
    geopy calculates the distance between 2 coordinates and returns the distance in km
    """
    return geopy.distance.geodesic(coords_1, coords_2).km

def get_nearby_bike_stations(place_name: str):
    """
    this function returns the nearest bike station based on the above function, calculate distance. 
    For loops through the stations in the object and obtains the lat long of each station. With the lat long, 
    we will use the calculate_distance function above to return the nearest station 
    """
    current_lat = get_user_lat_long(place_name)[1]
    current_lon = get_user_lat_long(place_name)[0]


    response = requests.get(STATION_INFO_URL).json()
    stations_array = response['data']['stations']

    current_coords = (current_lat, current_lon)
    stations_coords = [(s['lat'], s['lon']) for s in stations_array]
    distances = [calculate_distance(current_coords, station_coords) for station_coords in stations_coords]
    stations_distances = list(zip(stations_array, distances))
    stations_distances.sort(key=lambda s: s[1])
    names_distances = [(s[0]['name'], s[1]) for s in stations_distances]
    closest_ten = names_distances[:10]
    longest_name_len = len(max(closest_ten, key=lambda s: len(s[0]))[0])
    cool_output_prefix = f"NAME{' ' * longest_name_len}DISTANCE\n"
    cool_output_body = "\n".join(f"{s[0]} {' ' * (longest_name_len - len(s[0]))} {s[1]}" for s in closest_ten)
    cool_output = cool_output_prefix + cool_output_body
    return cool_output


def get_trip_price(minutes: int):
    if minutes <= 30:
        return "$2.95"
    else:
        price = 2.95
        dif = minutes - 30
        add = dif/30 + 1
        extra = math.floor(add)
        price = 2.95 + extra*4
        return f"${price}"

def get_json(url: str) -> dict:

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data

def main(): 
    """
    Test all the functions here
    """
    print(get_station_status('193'))
    print(get_user_lat_long('babson college'))
    print(get_avail_bikes('193'))
    print(get_station_information('3'))
    print(get_nearby_bike_stations('curry student center'))
    print(get_trip_price(15))
    print(get_trip_price(30))
    print(get_trip_price(31))
    print(get_trip_price(61))
    print(get_trip_price(1015))



if __name__ == '__main__':
    main()