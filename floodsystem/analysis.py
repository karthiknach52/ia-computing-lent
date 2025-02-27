from matplotlib.dates import date2num
import numpy as np


def polyfit(dates, levels, p):
    '''Find the least square fit polynomial to simulate the plot_water_level graph'''
    if len(dates) != len(levels):
        raise ValueError("Dates and levels are different lengths")
    x = date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, x[0]
