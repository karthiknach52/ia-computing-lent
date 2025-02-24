from matplotlib import dates
import numpy as np
def polyfit(dates, levels, p)
    time = dates.dates2num(dates)
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, x[0]
    