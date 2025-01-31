# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


import utils # noqa
from haversine import haversine, Unit


def calculate_distance(p, coordinates):
    return haversine(p, coordinates)


def stations_by_distance(stations, p):
    distance = []
    for i in range(len(stations)):
        distance.append(calculate_distance(stations[i].coord, p))
    stations_distance = list(zip(stations, distance))
    stations_distance = utils.sorted_by_key(stations_distance, 0)
    return stations_distance


def stations_within_radius(stations, centre, r):
    '''Return a list of all monitoring stations within a radius r of the centre co-ordinate'''
    out = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            out.append(station)
    return out
    