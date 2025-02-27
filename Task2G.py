from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_towns


stations = build_station_list()

towns = stations_by_towns(stations)
update_water_levels(stations)

town_to_mean_level = {}
for town in towns:

    levels = []
    for i in range(len(towns[town])):
        if towns[town][i].relative_water_level() is not None:
            levels.append(towns[town][i].relative_water_level())

    if len(levels) == 0:
        town_to_mean_level[town] = None
    else:
        town_to_mean_level[town] = sum(levels) / len(levels)

print(town_to_mean_level)
