from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

if __name__ == "__main__":
    stations = build_station_list()
    coord = (52.2053, 0.1218)
    radius = 10

    stations_in_radius = stations_within_radius(stations, coord, radius)
    station_names = [station.name for station in stations_in_radius]
    station_names.sort()

    print(station_names)
