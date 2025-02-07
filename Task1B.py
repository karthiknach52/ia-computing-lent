from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

if __name__ == "__main__":
    stations = build_station_list()
    print(stations_by_distance(stations, (52.2053, 0.1218)))
