# this file calls the API to get the blue bike details
import requests

STATION_DETAILS_URL = "https://gbfs.bluebikes.com/gbfs/en/station_status.json" 

# get station details 
def get_station_details(stat_id):
    response = requests.get(STATION_DETAILS_URL).json()
    stations_array = response['data']['stations']
    for station in stations_array:
        if station['station_id'] == stat_id :
            return station
    return("Station does not exist")

def get_station_status(stat_id):
    pass

def get_avail_bikes(stat_id):
    pass

def get_user_location():
    pass

def get_nearest_station():
    pass

def main(): 
    """
    Test all the functions here
    """
    print(get_station_details('193'))
   


if __name__ == '__main__':
    main()