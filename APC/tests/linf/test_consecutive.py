from codes.linf.consecutive import consecutive_and_sum


def test_consecutive():
    assert consecutive_and_sum(1, 1, 3) == "1 2 3\n6"
