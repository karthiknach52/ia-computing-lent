import floodsystem.flood as flood


def test_stations_level_over_threshold_empty_input():
    '''Check that an empty list returns an empty list'''
    assert flood.stations_level_over_threshold([], 1) == []


def test_stations_highest_rel_level():
    '''Check that an empty list returns an empty list'''
    assert flood.stations_level_over_threshold([], 10) == []
