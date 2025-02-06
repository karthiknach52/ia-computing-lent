from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    p = (52.2053, 0.1218)
    stations = build_station_list()
    print(stations_by_distance(stations, p))


if __name__ == "__main__":
    run()
