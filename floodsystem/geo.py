# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key # noqa
from haversine import haversine


def calculate_distance(p, coordinates):
    return haversine(p, coordinates)


def stations_by_distance(stations, p):
    distance = []
    name = []
    town = []
    for i in range(len(stations)):
        distance.append(calculate_distance(stations[i].coord, p))
        name.append(stations[i].name)
        town.append(stations[i].town)
    stations_distance = list(zip(name, town, distance))
    stations_distance = sorted_by_key(stations_distance, 2)
    stations_distance = stations_distance[:10]

    return stations_distance


def stations_within_radius(stations, centre, r):
    '''Return a list of all monitoring stations within a radius r of the centre co-ordinate'''
    out = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            out.append(station)
    return out


def rivers_with_station(stations):
    rivers = []
    for i in range(len(stations)):
        if stations[i].river not in rivers:
            rivers.append(stations[i].river)
        else:
            pass
    rivers.sort()
    return rivers


def stations_by_rivers(stations):
    test = {}
    for i in range(len(stations)):
        if stations[i].river not in test:
            test[stations[i].river] = []
        test[stations[i].river].append(stations[i].name)
    return test
           
            

            
        
        

