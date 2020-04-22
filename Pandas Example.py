#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import geocoder
import pandas as pd

def get_lat_lng(location):
    g = geocoder.osm('Mountain View, CA')
    return[g.json['lat'], g.json['lng']]
    
def get_forecast(latlong):
    apikey = '8847ac8ef5db4e7f96120512201504'
    url = 'http://api.weatherapi.com/v1/forecast.json'
    params = {'key': apikey, 'q': [latlong], 'days': 7}
    response = requests.get(url, params = params)
    results = response.json()['forecast']['forecastday']
    return(results)

def run_panda(days):
    weather = []
    for day in days:
        weather.append({'date': day['date'], 'Max Temperature': day['day']['maxtemp_f'], 'Min Temperature': day['day']['mintemp_f']})
    weather_data = pd.DataFrame(weather)
    return weather_data

# Main program
location = input("Enter your address here: ")
run_panda(get_forecast(get_lat_lng(location)))


# In[ ]:




