from codes.linf.parcelas import f_price


def test_parcelas():
    assert f_price(150, 4) == "165.00 41.25"
    assert f_price(200, 3) == "210.00 70.00"
    assert f_price(45, 1) == "42.75 42.75"
    assert f_price(70.25, 2) == "70.25 35.12"
