from codes.linf.fibofat import fibofat


def test_fibofat():
    assert fibofat(6) == "8 720 5"
    assert fibofat(10) == "55 3628800"
    assert fibofat(1) == "1 1"
