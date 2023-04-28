# this file calls the API to get the blue bike details
import requests
from config import MAPBOX_TOKEN
import json
import urllib.parse

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

#maybe forgo this, we can just let the user mention the bike station and return the state 
def get_nearby_bike_stations():
    pass

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
    print(get_station_information('193'))


if __name__ == '__main__':
    main()