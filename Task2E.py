from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
stations = build_station_list()
x = [i[0] for i in stations_highest_rel_level(stations, 5)]
dt = 10
for i in x:
    dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(i, dates, levels)
