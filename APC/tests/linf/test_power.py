from codes.linf.power import power


def test_power():
    assert power(2, 4) == 16
    assert power(4, 3) == 64
    assert power(5, 5) == 3125
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8
    assert power(100, 0) == 1
