from codes.challenges.painting import paint_price, round_up


def test_paint_price():
    assert paint_price(100) == ("160.00 R$", "150.00 R$", "105.00 R$")
    assert paint_price(200) == ("240.00 R$", "275.00 R$", "185.00 R$")


def test_round_up():
    assert round_up(1.5) == 2
    assert round_up(1.01) == 2
    assert round_up(1.99) == 2
    assert round_up(1) == 1
    assert round_up(2) == 2
