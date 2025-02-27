import floodsystem.plot as plot
from floodsystem.station import MonitoringStation


def test_plot_water_levels():
    '''Ensure no graphs are plotted when dates and levels are of different lengths'''
    station = MonitoringStation("s_id", "m_id", "label", (0, 0), (-1, 1), "river", "town")
    dates = [i for i in range(9)]
    levels = [i for i in range(10)]

    try:
        plot.plot_water_levels(station, dates, levels)
    except ValueError:
        assert True
        return

    assert False


def test_plot_water_level_with_fit():
    '''Ensure no graphs are plotted when dates and levels are of different lengths'''
    station = MonitoringStation("s_id", "m_id", "label", (0, 0), (-1, 1), "river", "town")
    dates = [i for i in range(9)]
    levels = [i for i in range(10)]
    p = None

    try:
        plot.plot_water_level_with_fit(station, dates, levels, p)
    except ValueError:
        assert True
        return

    assert False


# def test_polyfit():
#     '''Trying to make sure p is an integer and I don't know if this is a valid test'''
#     assert (type(p) == int)
