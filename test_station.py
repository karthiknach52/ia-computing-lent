# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_no_typical_range():
    '''Check that a missing typical range leads to marking as inconsistent'''
    # Station where the typical range is None
    assert not MonitoringStation("s_id", "m_id", "label", (0, 0), None, "river", "town").typical_range_consistent()


def test_nonsense_typical_range():
    '''Check that a nonsense typical range leads to marking as inconsistent'''
    # Station where the typical range high is lower than the low
    assert not MonitoringStation("s_id", "m_id", "label", (0, 0), (1, -1), "river", "town").typical_range_consistent()


def test_inconsistent_typical_range_empty_input():
    '''Check that an empty list returns an empty list'''
    assert inconsistent_typical_range_stations([]) == []
