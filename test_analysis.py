import floodsystem.analysis as analysis


def test_polyfit():
    '''Test that polyfit returns a valid polynomial'''
    a = [i for i in range(5)]
    poly, d = analysis.polyfit(a, a, 2)
    if poly(0) == float(0):
        assert True
        return
    assert False
