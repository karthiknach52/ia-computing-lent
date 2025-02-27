from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_towns, stations_within_radius
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from datetime import timedelta


def level_rising(station):
    '''Determine whether the level at a station is rising or fallng'''
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
    poly, d0 = polyfit(dates, levels, 4)
    if poly.deriv()(0) > 0:
        return True
    else:
        return False


def towns_to_risk(stations, threshold):
    '''Return a list of towns and associated risk level'''
    update_water_levels(stations)
    towns = stations_by_towns(stations)
    out = {}

    for town in towns:

        levels = []
        rising = False

        for station in towns[town]:
            if station.relative_water_level() is not None:
                levels.append(station.relative_water_level())
            if level_rising(station):
                rising = True

        if len(levels) != 0:
            avg = sum(levels) / len(levels)

            if avg > threshold:
                if rising:
                    out[town] = "Severe"
                    # Relative water level above the threshold and rising
                else:
                    out[town] = "Moderate"
                    # Relative water level above the threshold and falling
            else:
                out[town] = "Low"
                # Relative water level below the threshold

    return out


# Print station and associated risk for stations within 10km of Cambridge
stations = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
print(towns_to_risk(stations, 1))
