import floodsystem.geo as geo
from floodsystem.station import MonitoringStation

# Checks for stations_by_distance()
# NEED TO IMPLEMENT A CHECK TO TEST THAT THE LIST IS SORTED BY DISTANCE


def test_stations_by_distance_empty_list():
    assert geo.stations_by_distance([], (0, 0)) == []
    # if p != (float, float):
    #     raise ValueError("p should be a tuple of floats")


# Checks for stations_within_radius()


def test_check_stations_are_within_radius():
    '''Check that the distance functionality works correctly'''

    # Create a list of test stations
    # The last 2 stations in the list of 10 should be > 10km from (0, 0)
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    stations = [MonitoringStation(s_id, m_id, label, (0, i * 0.01), trange, river, town) for i in range(1, 11)]

    stations_in_radius = geo.stations_within_radius(stations, (0, 0), 10)

    assert len(stations_in_radius) == 8


def test_check_no_stations_in_radius_empty_list():
    '''Check that an empty list returns an empty list'''
    assert geo.stations_within_radius([], (0, 0), 10) == []

# NEED TO IMPLEMENT TESTS FOR:
# rivers_withs_station()
# stations_by_river()
# rivers_by_station_number()
