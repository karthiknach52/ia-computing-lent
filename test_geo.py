import floodsystem.geo as geo
from floodsystem.station import MonitoringStation


def test_stations_by_distance_empty_input():
    # DOCSTRING
    assert geo.stations_by_distance([], (0, 0)) == []
    # if p != (float, float):
    #     raise ValueError("p should be a tuple of floats")


def test_check_stations_in_radius():
    # Is this check necessary? Just repeating the function itself
    '''Check that the distance functionality works correctly'''

    # Create a list of test stations
    # The last 2 stations in the list of 10 should be > 10km from (0, 0)
    stations = [MonitoringStation("s_id", "m_id", "label", (0, i * 0.01), (-1, 1), "river", "town")
                for i in range(1, 11)]

    stations_in_radius = geo.stations_within_radius(stations, (0, 0), 10)

    assert len(stations_in_radius) == 8


def test_check_stations_in_radius_empty_input():
    '''Check that an empty list returns an empty list'''
    assert geo.stations_within_radius([], (0, 0), 10) == []


# NEED TO IMPLEMENT TESTS FOR:
# rivers_withs_station()
# stations_by_river()


def test_rivers_by_station_number_empty_input():
    '''Check that an empty list returns an empty list'''
    assert geo.rivers_by_station_number([], 10) == []


def test_rivers_by_station_number_most_stations():
    '''Check that the first river has the most stations'''
    # Create a list of test 15 stations which are on 5 different rivers
    stations = [MonitoringStation("s_id", "m_id", "label", (0, 0), (-1, 1), "river" + str(i), "town")
                for i in [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]]

    assert geo.rivers_by_station_number(stations, 3)[0][1] == 5


def test_rivers_by_station_number_length_N():
    '''Check that only N rivers are returned (edge case tested below)'''
    # Create a list of test 15 stations which are on 5 different rivers
    stations = [MonitoringStation("s_id", "m_id", "label", (0, 0), (-1, 1), "river" + str(i), "town")
                for i in [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]]

    assert len(geo.rivers_by_station_number(stations, 3)) == 3


def test_rivers_by_station_number_correct_length():
    '''Check that rivers with the same number of stations as the Nth river are included'''
    # Create a list of test 10 stations which are on 5 different rivers
    stations = [MonitoringStation("s_id", "m_id", "label", (0, 0), (-1, 1), "river" + str(i % 5), "town")
                for i in range(1, 11)]

    assert len(geo.rivers_by_station_number(stations, 3)) == 5
