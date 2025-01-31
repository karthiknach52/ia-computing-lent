from floodsystem.stationdata import build_station_list
import floodsystem.utils # noqa
from haversine import haversine, Unit
def run():
    p = (52.2053, 0.1218)
    stations = build_station_list()
    print(stations_by_distance(stations, p))
def calculate_distance(p, coordinates):
    return haversine(p, coordinates)


def stations_by_distance(stations, p):
    distance = []
    name = []
    town = []
    for i in range(len(stations)):
        distance.append(calculate_distance(stations[i].coord, p))
        name.append(stations[i].name)
        town.append(stations[i].town)
    stations_distance = list(zip(name, town, distance))
    stations_distance = floodsystem.utils.sorted_by_key(stations_distance, 2)
    stations_distance = stations_distance[:10]

    return stations_distance


if __name__ == "__main__":
    run()