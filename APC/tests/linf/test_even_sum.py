from codes.linf.even_sum import even_sum


def test_even_sum():
    assert even_sum(13) == 2 + 4 + 6 + 8 + 10
    assert even_sum(20) == 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18
    assert even_sum(-6) == -1
