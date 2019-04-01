#Ugyen Dorji, 83628422, udorji@uci.edu


#------MapQuest API Access------
import json
import urllib.parse
import urllib.request
import NaviClasses


NC=NaviClasses


MAPQUEST_API_KEY='WIfx2ZkRBs0GG9l0WCYH8bxjRU2Rt2F5'
CONSUMER_SECRET='5ZA5bOM9Rt6HIjOq'
BASE_MAPQUEST_URL='http://open.mapquestapi.com/'


def build_directions_url() -> str:
    '''
    This function takes the destinations, and builds and returns a URL that can be used to ask the
    MapQuest direction API for information about STEPS, TOTALDISTANCE, TOTALTIME and LATLONG;for each destination.
    '''
    lst_destinations=destinations()    
    start=lst_destinations[0]
    url_parameters = [('key', MAPQUEST_API_KEY), ('from', start)]

    for dest_index in range(len(lst_destinations)-1):
        destination=lst_destinations[dest_index+1]
        url_parameters.append(('to', destination))
    return BASE_MAPQUEST_URL +'directions/v2/route?' + urllib.parse.urlencode(url_parameters)


def build_elevation_url(result:dict) -> str:
    '''
    This function takes the resulting url created by the build_directions_url function to get a
    string from NC.ELEVATION.get_latLng() , it then builds and returns a URL that can be used to ask the
    MapQuest elevation API for information about elevation for each destination
    request.
    '''
    LatLngs=NC.ELEVATION.get_latLng(result)
    url_parameters = [('key', MAPQUEST_API_KEY), ('shapeFormat', 'raw'), ('latLngCollection', LatLngs)]
    return BASE_MAPQUEST_URL +'elevation/v1/profile?' + urllib.parse.urlencode(url_parameters)



def get_result(url: str) -> dict:
    '''
    Takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    except:
            print()
            print('MAPQUEST ERROR')
        
    finally:
        if response != None:
            response.close()


def destinations()->list:
    '''
    Asks for number of destinations, then asks for each destination and finally creates and
    returns a list of the destinations.
    '''
    num_destinations=int(input())
    destinations=[]
    for destination in range(num_destinations):
        destination=input()
        destinations.append(destination)
    return destinations


def travelCalcs()->['travel calcs']:
    '''
    Asks for the number of outputs, then asks for specific outputs desired and finally creates
    and returns a list of the desired outputs.
    '''
    num_outputs=int(input())
    travel_calcs=[]
    for output in range(num_outputs):
        travel_calc=input()
        travel_calcs.append(travel_calc)
    return travel_calcs    


def run_calcs(result:dict):
    '''
    Takes list of desired outputs and matches the it to a key in the travel_calc_dict to use the function
    of the key it is matched with. Uses the function to calculate the wanted outputs.
    '''
    travel_calcs=travelCalcs()
    travel_calc_dict={'STEPS':NC.STEPS,'TOTALDISTANCE':NC.TOTALDISTANCE, 'TOTALTIME':NC.TOTALTIME,
                      'LATLONG':NC.LATLONG, 'ELEVATION':NC.ELEVATION}
    wanted_value = None
    for travel_calc in travel_calcs: 
            calc=travel_calc_dict[travel_calc]
            wanted_value = calc.calculate(result)


def error_check(result:dict):
    '''
    Checks for errors by finding the key routeError if it is found the function returns True meaning that
    there was an error and hence printing an error messsage; also the returned boolean cause the program to end.
    If a typeerrror is returned it means that build_directions_url returned a none type and thus an mapquest error
    occured within the build url error and the program ends. If all is good and nothing goes wrong the fucntion
    returns False, thus allowing the program to fully execute. 
    '''
    try:
        result=result['route']
        for error in result:
            if error=='routeError':
                print()
                print('NO ROUTE FOUND')
                return True
                break
            else:
                return False
                break
    except TypeError:
        print()
