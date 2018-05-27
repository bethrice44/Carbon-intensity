#!/usr/bin/env python

"""
Extract data from National Grid Carbon Intensity API

"""

import requests
import sys


def carbon_intensity(start, end):
    """ Start and end times in YYYY-MM-DDThh:mmZ format """

    headers = {'Accept': 'application/json'}

    r = requests.get('https://api.carbonintensity.org.uk/intensity/start/end',
                     params={}, headers=headers)

    print r.json()

    return r


def get_factors():
    """ Get carbon intensity factors for each fuel type, in gCO2/kWh """

    headers = {'Accept': 'application/json'}

    r = requests.get('https://api.carbonintensity.org.uk/intensity/factors',
                     params={}, headers=headers)

    print r.json()

    return r


def stats(start, end):
    """ Get carbon intensity stats (max,min,average,index) for date range """

    headers = {'Accept': 'application/json'}

    r = requests.get('https://api.carbonintensity.org.uk/stats/start/end',
                     params={}, headers=headers)

    print r.json()

    return r


def main():
    start = sys.argv[1]
    end = sys.argv[2]
    print carbon_intensity(start, end)


main()
