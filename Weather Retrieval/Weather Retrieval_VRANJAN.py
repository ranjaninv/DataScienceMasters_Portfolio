# Title : Week12 - Programming Assignment
# Author : Vikas Ranjan
# Date : 5/25/2020
# Purpose : We will be creating an application to interacts with a webservice in order to obtain data. Program will use all of the information we’ve learned in the class in order to create a useful application.
#           Program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap. Program must display the weather information in a READABLE format to the user.
#               Create a header for your program just as you have in the past.
#               Create a Python Application which asks the user for their zip code or city.
#               Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
#               Display the weather forecast in a readable format to the user.
#               Use comments within the application where appropriate in order to document what the program is doing.
#               Use functions including a main function.
#               Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
#               Validate whether the user entered valid data. If valid data isn’t presented notify the user.
#               Use the Requests library in order to request data from the webservice.
#               Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
#               Use Python 3
#               Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.

import requests
import datetime
import json

def parse_json(json_response, city_zip):
        # Retrieve relvent weather data, Looking at this data in debug mode helped parse and convert it properly
        main = json_response["main"]
        city = json_response["name"]
        cur_weather = json_response["weather"]
        cur_temp = main["temp"]
        min_temp = main["temp_min"]
        max_temp = main["temp_max"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        # Convert Kalvin Temperature to Fahrenheit
        cur_temp_f = int(float((9 * (cur_temp - 273.15))/5 + 32))
        max_temp_f = int(float((9 * (max_temp - 273.15))/5 + 32))
        min_temp_f = int(float((9 * (min_temp - 273.15))/5 + 32))
        sys = json_response['sys']
        sunrise = sys['sunrise']
        sunset = sys['sunset']
        country = sys['country']
        # Convert time to standard format
        sunrise_time = datetime.datetime.fromtimestamp(int(sunrise)).strftime('%I:%M %p')
        sunset_time = datetime.datetime.fromtimestamp(int(sunset)).strftime('%I:%M %p')
        winds = json_response['wind']
        wind_speed = winds['speed']
        # Convert wind speed from meters per second to miles per hour
        windSpeed_miles = round(wind_speed * 2.237)
        print('Wind Speed   :', str(windSpeed_miles), 'mph')
        print('Humidity     :', str(humidity) + '%' + '\n')
        # Pretty Print of the Weather
        print('{0} {1}'.format('Current Weather conditions for', city_zip))
        print('Current Temp :', str(cur_temp_f) +'\u00b0F')
        print('High Temp    :', str(max_temp_f) + '\u00b0F')
        print('Low Temp     :', str(min_temp_f) + '\u00b0F')
        print('Sunrise      :', sunrise_time)
        print('Sunset       :', sunset_time)
        for item in cur_weather:
            print('Cloud Cover  :', (item['description']))

def fetchWeather(city_zip, option):
    # Generated API key
    api_key = "3217aecfb7a1e71fda0ba81b086a2e7d"
    # url for open weather API
    url = "https://api.openweathermap.org/data/2.5/weather?"
    # test connection
    try:
        testconn = requests.get(url + api_key)
        testconn.raise_for_status()
        if testconn.status_code == 200:

            # complete url with API key and City name or zip code
            if option == '1':
                url = url + "appid=" + api_key + "&q=" + city_zip
            elif option == '2':
                url = url + "appid=" + api_key + "&zip=" + city_zip
                # Invoke get to fetch weather info for the desired city
            try:
                response = requests.get(url)
                response.raise_for_status()
                # convert json format
                json_response = response.json()
                if response.status_code == 200:
                    parse_json(json_response, city_zip)
            except requests.exceptions.HTTPError as err:
                if response.status_code == 404:
                    if option == '1':
                        print("City not found, please enter a valid City Name for weather lookup!!\n")
                    elif option == '2':
                        print("City not found, please enter a valid Zip Code for weather lookup!!")
                else:
                    print ("Http Error:",err)
            except requests.exceptions.ConnectionError as err:
                print ("Error Connecting:",err)
            except requests.exceptions.Timeout as err:
                print ("Timeout Error:",err)
            except requests.exceptions.RequestException as err:
                print ("unknown Error:",err)
        else:
            print('Connection was not successful, please try again!')
    except requests.exceptions.HTTPError as e:
        print('Connection was not successful, please try again!')
        return "Error: " + str(e)

def main():
    # Welcome message
    print("Welcome to the Python weather forecast application!\n")
    anotherLookup = True
    while anotherLookup == True:
        option = input("Would you like to lookup weather data by US city or zip code? Enter 1 for US City 2 for zip: ")
        if option == '1':
            city = input('Please enter the city name: ')
            fetchWeather(city, option)
        elif option == '2':
            zip = input('Please enter the Zip Code: ')
            fetchWeather(zip, option)
        else:
            print("Invalid input, please select a valid choice")

        while True:
            if option == '1' or option == '2':
                anotherLookup = input("\nWould you like to perform another weather lookup? (Y/N) ")
                if anotherLookup.upper() == 'Y':
                    anotherLookup = True
                    break;
                elif anotherLookup.upper() == 'N':
                    anotherLookup = False
                    break;
                else:
                    print("Please enter a valid choice (Y/N)")

if __name__ == '__main__':
    main()



