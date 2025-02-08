from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

stations, levels = zip(*stations_highest_rel_level(build_station_list(), 10))

for i in range(len(stations)):
    print(stations[i].name, levels[i])
