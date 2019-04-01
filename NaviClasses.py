#Ugyen Dorji, udorji@uci.edu, 83628422


#------NAVIGATION CLASSES------
import MapQuestAPI
MQ=MapQuestAPI


class STEPS:
    def calculate(result:dict)->str:
        '''
        Finds the directions by iterating through a series of nested dictionaries and lists
        till it finds the needed information in this case maneuvers then narrative. Once the
        values of the narratives are accessed it is printed
        '''
        x={'y': {}}
        print('DIRECTIONS')
        result=result['route']['legs']
        for x in range(len(result)):
            for y in result[x]:
                if y=='maneuvers':
                    for z in range(len(result[x][y])):
                        for a in result[x][y][z]:
                            if a=='narrative':
                                print(result[x][y][z][a])
        print()
        
        
class TOTALDISTANCE:
    def calculate(result:dict)->int:
        '''
        Accesses the value of distance through the keys route and distance of the result
        dictionary,which was created by the MQ.get_url function. Finally turns the value into
        an integer, rounds to the nearest whole number and prints the resulting value.
        '''
        result=result['route']['distance']
        result=round(int(result))
        print('TOTAL DISTANCE: {} miles'.format(result))
        print()
        
        
class TOTALTIME:
    def calculate(result:dict):
        '''
        Accesses the value of time through the keys route and time of the result
        dictionary. Turns the value into an integer, converts to minutes, rounds to the nearest whole number
        and prints the resulting value.
        '''
        result=result['route']['time']
        result=round(int(result)/60)
        print('TOTAL TIME: {} minutes'.format(result))
        print()


class LATLONG:
    def calculate(result:dict):
        '''
        Accesses the value of locations through the keys route and locations of the result
        dictionary. Iterates thorugh the loactions, then iterates through each dictionary within the list
        till it finds the key latLng. Finally iterates through the latLng dictionary, turns the
        values of of lattitude and longitude into a int, rounds it and prints out the resulting value.
        '''
        print('LATLONGS')
        result=result['route']['locations']
        for x in range(len(result)):
            for y in (result[x]):
                if y=='latLng':
                    for z in (result[x][y]):
                        latlng=round(int(result[x][y][z]))
                        print(latlng)
        print()     
        

class ELEVATION:
    def calculate(result:dict):
        '''
        Takes the library returned by the build_elevation_url function and accesses elevationProfile
        list, then it iterates through each of the nested dictionaries till it finds the key, height,
        finally it rounds the height and prints the value.            
        '''
        print('ELEVATIONS')
        elevation_result=MQ.get_result(MQ.build_elevation_url(result))
        elevation_result=elevation_result['elevationProfile']
        for distHeight in range(len(elevation_result)):
            for Height in elevation_result[distHeight]:
                if Height=='height':
                    elevation=round(int(elevation_result[distHeight][Height]))
                    print(elevation)
        print()
                    
            
    def get_latLng(result:dict):
        '''
        Creates a nested list of latitude and longitude, and then creates a string of the
        latitudes and longitudes in the order of longitude then latitude to be used as a parameter
        in the build_elevation_url.   
        '''
        latLngs=[]
        mini_latLngs=[]
        latLngs_str=''
        result=result['route']['locations']
        for x in range(len(result)):
            for y in (result[x]):
                if y=='latLng':
                    for z in (result[x][y]):
                        latlng=result[x][y][z]
                        mini_latLngs.append(latlng)
                    if len(mini_latLngs)==2:
                        latLngs.append(mini_latLngs)
                        mini_latLngs=[]
        for x in latLngs:
            Lng=str(x[0])
            lat=str(x[1])
            latLngs_str+=lat+','+Lng+','
        latLngs_str=latLngs_str[:-1]
        return latLngs_str
        
        
