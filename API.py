# Ngoc Nguyen ID# 72114439 LAB 3 PROJECT 3


import json
import urllib.parse
import urllib.request
import API_classes


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

def printing_check(number: int)-> int:
    ''' Return a proper number that is greater than or equal to input'''

    try:
        user_input= int(input())
        if user_input >= number:
            return user_input
        else:
            print('The input is out of range.')
    except:
        print('The input is invalid.')

            
def check_and_store_data(number: int)-> list:
    ''' Return a list of data after verifying the input'''
    
    information_list = []

    for item in range(number):
        info = input()
        if info.strip() == '':
            print('The input is invalid')
            information_list = []
            return information_list
            
        else:
            information_list.append(info.strip())
                
    return information_list
        

                

def run_API()-> None:
    ''' Run the module using the functions defined above'''

    try:

        location_number = printing_check(2)

        location_list = check_and_store_data(location_number)
                              
        url = format_url(location_list)
        new_url= json_url(url)
        
        printing_option = printing_check(1)
        printing_option_list = check_and_store_data(printing_option)

        for item in printing_option_list:
            if item not in ['LATLONG', 'STEPS', 'TOTALDISTANCE', 'TOTALTIME']:
                print('The input {} is invalid.'.format(item))
                return 
                
        API_classes.run_generate(printing_option_list, new_url, location_number)       

    except:
        pass
            
    finally:
        print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    


