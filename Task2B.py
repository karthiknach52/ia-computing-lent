from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

stations, levels = zip(*stations_level_over_threshold(build_station_list(), 0.8))

for i in range(len(stations)):
    print(stations[i].name, levels[i])
