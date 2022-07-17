from codes.linf.mmc import mmc


def test_mmc():
    assert mmc([9, 30]) == 90
    assert mmc([30, 9]) == 90
    assert mmc([8, 12]) == 24
