from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
stations = build_station_list()


def run():
    # THIS IS NOT COMPLETE
    River_Cam_stations = sorted(stations_by_river(stations)['River Cam'])
    print(River_Cam_stations)


if __name__ == "__main__":
    run()
