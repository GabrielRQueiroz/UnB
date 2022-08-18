from codes.challenges.is_messy import is_messy


def test_is_messy():
    movements = [
        "A D 2",
        "A E 1",
        "B D 1",
        "A D 0",
        "C E 0",
    ]

    assert is_messy("A B C", movements) == 0

    movements = [
        "X D 3",
        "Y D 1",
        "W E 1",
        "Z E 0",
        "W E 1",
    ]

    assert is_messy("X Y Z W", movements) == 4
