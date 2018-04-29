#!/usr/bin/env python

"""
Extract data from National Grid Carbon Intensity API

"""

import requests



def Carbon_intensity(start,end):
    """ Start and end times in YYYY-MM-DDThh:mmZ format """

    headers = {'Accept': 'application/json'}

    r = requests.get('https://api.carbonintensity.org.uk/intensity/start/end', params={}, headers = headers)

    print r.json()

    return r



def Get_factors():
    """ Get carbon intensity factors for each fuel type, in gCO2/kWh """

    headers = {'Accept': 'application/json'}

    r = requests.get('https://api.carbonintensity.org.uk/intensity/factors', params={}, headers = headers)

    print r.json()

    return r



def Stats(start,end):
    """ Get statistics (max, min, average, index) for carbon intensity for a date range """

    headers = {'Accept': 'application/json'}
    
    r = requests.get('https://api.carbonintensity.org.uk/stats/start/end', params={}, headers = headers)
    
    print r.json()
    
    return r