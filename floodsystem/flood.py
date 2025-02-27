from .stationdata import update_water_levels


def stations_level_over_threshold(stations, tol):
    '''Returns a list of stations and their relative water levels if they are higher than the threshold'''
    out = []
    update_water_levels(stations)
    for station in stations:
        if station.latest_level:
            if station.latest_level > tol:
                out.append((station, station.relative_water_level()))

    return out


def stations_highest_rel_level(stations, N):
    '''Returns a list of the N stations with the highest relative water level'''
    out = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() is not None:
            out.append((station, station.relative_water_level()))

    out = sorted(out, key=lambda x: x[1], reverse=True)
    return out[:N]
