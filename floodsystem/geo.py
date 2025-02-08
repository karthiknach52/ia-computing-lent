# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    '''Return a list of stations sorted by distances'''
    distance = []
    name = []
    town = []
    for i in range(len(stations)):
        distance.append(haversine(stations[i].coord, p))
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
    '''Return all the rivers that have at least 1 station '''
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers


def stations_by_river(stations):
    '''Return a dictionary that maps all the rivers to the stations on it'''
    test = {}
    for i in range(len(stations)):
        if stations[i].river not in test:
            test[stations[i].river] = []
        test[stations[i].river].append(stations[i].name)
    return test


def rivers_by_station_number(stations, N):
    '''Returns the N rivers with the most stations'''
    river_dict = stations_by_river(stations)
    rivers = [(river, len(river_dict[river])) for river in river_dict]
    sorted_rivers = sorted(rivers, key=lambda x: x[1], reverse=True)
    out = sorted_rivers[:N]

    # Add rivers if they have the same number of stations as the Nth river
    while len(out) < len(sorted_rivers) and sorted_rivers[len(out)][1] == sorted_rivers[N - 1][1]:
        out.append(sorted_rivers[len(out)])

    return out
