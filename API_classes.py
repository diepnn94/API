# Ngoc Nguyen ID# 72114439 LAB 3 PROJECT 3


class STEPS:

    def __init__(self, url: 'json'):
        '''Initializes an url'''
        self._url = url
        
    def generate(self, location_num:int)-> None:
        ''' Print out the steps listed in the URL'''
        print('\nDIRECTIONS')
        for location in range(0, location_num-1):
            for item in self._url['route']['legs'][location]['maneuvers']:
                print(item['narrative'])
                

class TOTALDISTANCE:

    def __init__(self, url: 'json'):
        '''Initializes an url'''
        self._url = url
        
    def generate(self, location_num:int)-> None:
        ''' Print out the total distance in mile for the trip'''
        mileage = 0
        for location in range(0, location_num-1):
            for item in self._url['route']['legs'][location]['maneuvers']:
                mileage+= item['distance']
        print('\nTOTAL DISTANCE: {} miles'.format(round(mileage)))

class TOTALTIME:

    def __init__(self, url: 'json'):
        '''Initializes an url'''
        self._url = url
        
    def generate(self, location_num:int)-> None:
        '''Print out the total time in minute for the trip'''
        time = 0
        for location in range(0, location_num-1):
            for item in self._url['route']['legs'][location]['maneuvers']:
                time += item['time']
        print('\nTOTAL TIME: {} minutes'.format((round(time/60))))

class LATLONG:

    def __init__(self, url: 'json'):
        '''Initializes an url'''
        self._url = url
        
    def generate(self, location_num: int)-> None:
        ''' Print out the latitude and and longitude for each specified location'''
        print()
        for location in range(0, location_num):
            longtitude = (self._url['route']['locations'][location]['latLng']['lng'])
            latitude = (self._url['route']['locations'][location]['latLng']['lat'])


            new_longtitude = round(longtitude,2)
            long_dir= 'E'

            new_latitude= round(latitude,2)
            lat_dir= 'N'

            if longtitude < 0:
                new_longtitude = round(longtitude*(-1),2)
                long_dir = 'W'                     
            elif latitude < 0:
                new_latitude = round(latitude*(-1),2)
                lat_dir = 'S'
                
            print("{:.2f}{} {:.2f}{}".format(new_latitude, lat_dir, new_longtitude, long_dir))



def run_generate(steps: ['step'], url:'json', location_num: int)-> None:
    ''' Print the calculation for each cal specified above'''
    
    for step in steps:
        if step == 'LATLONG':
            item = LATLONG(url)
        elif step == 'TOTALTIME':
            item = TOTALTIME(url)
        elif step == 'TOTALDISTANCE':
            item = TOTALDISTANCE(url)
        elif step == 'STEPS':
            item = STEPS(url)
        else:
            pass
        item.generate(location_num)

    
        
