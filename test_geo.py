from haversine import haversine
import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    coord = (52.2053, 0.1218)
    assert geo.stations_by_distance([], coord) == []
    if p != (float, float):
        raise ValueError("p should be a tuple of floats")


def test_stations_within_radius():
    stations = build_station_list()
    coord = (52.2053, 0.1218)
    radius = 10

    stations_in_radius = geo.stations_within_radius(stations, coord, radius)

    for station in stations_in_radius:
        if haversine(station.coord, coord) > radius:
            assert False

    assert True

