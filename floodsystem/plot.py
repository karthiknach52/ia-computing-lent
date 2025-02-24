import matplotlib.pyplot as plt
import matplotlib


def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    time = matplotlib.dates.date2num(dates)
    plt.plot(time, levels)
    plt.plot(time, p(time - time[0]))
    plt.xlabel('dates')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
