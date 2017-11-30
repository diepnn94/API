# Ngoc Nguyen ID# 72114439 LAB 3 PROJECT 3


import json
import urllib.parse
import urllib.request
import classes


KEY = "Fmjtd%7Cluu821682u%2Caa%3Do5-942n0u" 
MAP_BASE = 'http://open.mapquestapi.com/directions/v2/route?key=' + KEY + "&"

def format_url(location: [str])->str:
    ''' Return a properly formated url that is converted to URL query parameters'''

    destination =[('from',location[0])]
    for item in range(1,len(location)):
        destination.append(('to',location[item]))
                         
    url = MAP_BASE + urllib.parse.urlencode(destination)
    new_url = url.replace('%2C',',')
    return new_url

#print(format_url(['616 Flintstone DR','Huntington Beach','Las Vegas']))

def json_url(url: str)-> 'json':
    ''' Return the url in JSON text'''

    response= None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response!= None:
            response.close()

#print(json_url(format_url(['616 Flintstone DR','Huntington Beach','Las Vegas'])))

def steps(url:'json', location_num: int)-> None:
    ''' Print out the steps listed in the URL'''
    print('\nDIRECTIONS\n')
    for location in range(0, location_num-1):
        for item in url['route']['legs'][location]['maneuvers']:
            print(item['narrative'])
            print()

              

#steps(json_url(format_url(['616 Flintstone DR','Huntington Beach','Las Vegas'])),3)

def distance(url:'json', location_num: int)-> None:
    ''' Print out the total distance in mile for the trip'''
    mileage = 0
    for location in range(0, location_num-1):
        for item in url['route']['legs'][location]['maneuvers']:
            mileage+= item['distance']
    print('\nTOTAL DISTANCE: {} miles'.format(int(mileage)))

#distance(json_url(format_url(['616 Flintstone DR','Huntington Beach','Las Vegas'])),3)

def time(url:'json', location_num: int)-> None:
    '''Print out the total time in minute for the trip'''
    time = 0
    for location in range(0, location_num-1):
        for item in url['route']['legs'][location]['maneuvers']:
            time += item['time']
    print('\nTOTAL TIME: {} minutes'.format(int(round(time/60,0))))

#time(json_url(format_url(['616 Flintstone DR','Huntington Beach','Las Vegas'])),3)

def latlong(url: 'json', location_num: int)-> None:
    ''' Print out the latitude and and longitude for each specified location'''

    for location in range(0, location_num):
        longtitude = (url['route']['locations'][location]['latLng']['lng'])
        latitude = (url['route']['locations'][location]['latLng']['lat'])


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

        print("\n{:.2f}{} {:.2f}{}".format(new_latitude, lat_dir, new_longtitude, long_dir))



#latlong(json_url(format_url(['616 Flintstone DR','Huntington Beach','Las Vegas'])),3)


def location_check()-> int:
    ''' Return a properly formatted number that is at least equal to or greater than the input'''
    while True:
        try:
            user_input= int(input('How many destination?: '))
            if user_input >= 2:
                return user_input
            else:
                print('The input is invalid.')
        except:
            print('The input is invalid.')

            
def check_and_store_data(number: int)-> list:
    ''' Return a list of data after verifying the input'''

    information_list = []
    while True:    
        for item in range(number):
            info = input('Input: ')
            information_list.append(info.strip())

        if len(information_list)== number:
            return information_list
        else:
            print('The numbers of destination did not match with the number orginally specified, please enter the correct number')

def printing_check()-> int:
    ''' Return a proper number that is greater than or equal to 1'''

    while True:
        try:
            user_input= int(input('how many choices: '))
            if user_input>= 1:
                return user_input
            else:
                print('The input is out of range.')
        except:
            print('The input must be an interger greater than or equal to 1.')
                

def handling(url: 'json', number: int, printing_list: list)-> None:
    ''' Print out the information that corrosponds to the input'''
    
        
    for item in printing_list:
        if item == "STEPS":
            steps(url, number)
        elif item == "TOTALDISTANCE":
            distance(url,number)
        elif item == "TOTALTIME":
            time(url, number)
        elif item== "LATLONG":
            latlong(url, number)
        else:
            pass
    print()


if __name__ == '__main__':


    try:

        location_number = location_check()

        location_list = check_and_store_data(location_number)
                              
        url = format_url(location_list)
        new_url= json_url(url)
        
        printing_option= printing_check()
        printing_option_list = check_and_store_data(printing_option)

        classes.run_calcs(printing_option_list, new_url, location_number)

        #handling(new_url, location_number, printing_option_list)

    except:
        pass
            
    finally:
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

