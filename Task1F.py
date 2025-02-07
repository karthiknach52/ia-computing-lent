from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

if __name__ == "__main__":
    stations = inconsistent_typical_range_stations(build_station_list())
    station_names = [station.name for station in stations]
    station_names.sort()
    print(station_names)
