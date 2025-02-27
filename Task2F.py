from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()
x = [i[0] for i in stations_highest_rel_level(stations, 5)]
dt = 2
for i in x:
    dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, 4)
    plot_water_level_with_fit(i, dates, levels, poly)
