import matplotlib.pyplot as plt
from matplotlib.dates import date2num, num2date


def plot_water_levels(station, dates, levels):
    '''Plot the relative water level against dates'''
    if len(dates) != len(levels):
        raise ValueError("Dates and levels are different lengths")
    plt.axhline(y=0.0, color='r', linestyle='dotted')
    plt.axhline(y=1.0, color='y', linestyle='dotted')
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    '''Plot the relative water level along with the least square fit polynomial against dates'''
    time = date2num(dates)
    if len(dates) != len(levels):
        raise ValueError("Dates and levels are different lengths")
    plt.axhline(y=0.0, color='r', linestyle='dotted')
    plt.axhline(y=1.0, color='y', linestyle='dotted')
    plt.plot(num2date(time), levels, 'o')
    plt.plot(num2date(time), p(time - time[0]), 'b')
    plt.xlabel('dates')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
