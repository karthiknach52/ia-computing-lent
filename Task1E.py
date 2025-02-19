from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

if __name__ == "__main__":
    stations = build_station_list()
    print(rivers_by_station_number(stations, 10))
