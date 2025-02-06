from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_rivers
stations = build_station_list()


def run1():
    return rivers_with_station(stations)
    

def run2():
    return stations_by_rivers(stations)

River_Cam_stations = sorted(stations_by_rivers(stations)['River Cam'])
print(River_Cam_stations)

if __name__ == "__main__":
    run2()
