import floodsystem.analysis as analysis


def test_polyfit():
    '''Test that no polynomial is returned when dates and levels are not the same length'''
    dates = [i for i in range(9)]
    levels = [i for i in range(10)]

    try:
        analysis.polyfit(dates, levels, 2)
    except ValueError:
        assert True
        return

    assert False
