from floodsystem.plot import plot_water_levels
import datetime
from floodsystem.analysis import polyfit
def test_plot_water_levels(dates, levels):
    '''Ensure no graphs are plotted when dates and levels are of different lengths but I don't know how to do this and I guess we could do the same with plot_water_level_with_fit?'''
    assert (len(dates) == len(levels))


def test_polyfit():
    '''Trying to make sure p is an integer and I don't know if this is a valid test'''
    assert (type(p) == int)






    