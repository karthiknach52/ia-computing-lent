# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   latest level:  {}\n".format(self.latest_level)
        d += "   rel level:     {}".format(self.relative_water_level())
        return d

    def typical_range_consistent(self):
        '''Returns True if the typical_range exists and makes sense'''
        if self.typical_range is not None:
            if self.typical_range[0] <= self.typical_range[1]:
                return True
        return False

    def relative_water_level(self):
        '''Returns the latest water level as a fraction of the typical min and max'''
        if self.typical_range_consistent() and self.latest_level:
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
        else:
            return None


def inconsistent_typical_range_stations(stations):
    '''Return a list of stations whose typical_range is inconsistent'''
    return [station for station in stations if not station.typical_range_consistent()]
