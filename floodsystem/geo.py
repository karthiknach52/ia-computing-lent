# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_within_radius(stations, centre, r):
    '''Return a list of all monitoring stations within a radius r of the centre co-ordinate'''
    out = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            out.append(station)

    return out
