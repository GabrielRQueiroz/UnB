from codes.challenges.forth_back import forth_back


def test_forth_back(capfd):
    forth_back(5)
    out1, err1 = capfd.readouterr()
    forth_back(1)
    out2, err2 = capfd.readouterr()
    forth_back(2)
    out3, err3 = capfd.readouterr()

    assert out1 == "1\n12\n123\n1234\n12345\n12345\n1234\n123\n12\n1\n"
    assert out2 == "1\n1\n"
    assert out3 == "1\n12\n12\n1\n"
