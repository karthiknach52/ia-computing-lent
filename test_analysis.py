import floodsystem.analysis as analysis


def test_polyfit():
    '''Test that polyfit returns a polynomial'''
    a = [i for i in range(5)]
    poly, d = analysis.polyfit(a, a, 2)
    if poly(0) != 0:
        assert False
        return
    assert True
