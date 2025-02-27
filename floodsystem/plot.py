import matplotlib.pyplot as plt
import matplotlib

# NEEDS DOCSTRINGS AND HIGH AND LOW NEED TO BE UPDATED


def plot_water_levels(station, dates, levels):
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
    time = matplotlib.dates.date2num(dates)
    plt.axhline(y=0.0, color='r', linestyle='dotted')
    plt.axhline(y=1.0, color='y', linestyle='dotted')
    plt.plot(time, levels, 'o')
    plt.plot(time, p(time - time[0]), 'b')
    plt.xlabel('dates')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
