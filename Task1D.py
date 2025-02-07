from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

if __name__ == "__main__":
    # THIS IS NOT COMPLETE
    stations = build_station_list()
    River_Cam_stations = sorted(stations_by_river(stations)['River Cam'])
    print(River_Cam_stations)
