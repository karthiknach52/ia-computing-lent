from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

if __name__ == "__main__":
    stations = build_station_list()

    rivers = list(rivers_with_station(build_station_list()))
    rivers.sort()
    print(rivers[:10])

    print(sorted(stations_by_river(stations)['River Cam']))
    print(sorted(stations_by_river(stations)['River Aire']))
    print(sorted(stations_by_river(stations)['River Thames']))
