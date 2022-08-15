from codes.challenges.beijo_da_vo import prize


def test_prize():
    clients = {"Roberto": 2, "Júlia": 2, "Umbreon": 1, "Blackout": 0}

    assert prize(4, 3, clients) == "Júlia"
    assert prize(4, 2, clients) == "Roberto"
    assert prize(4, 1, clients) == "Umbreon"

    clients = {"Abacatilson": 0, "Vigário": 0, "Joelma": 0}

    assert prize(3, 0, clients) == "Abacatilson"
