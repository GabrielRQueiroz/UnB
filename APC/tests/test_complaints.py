from complaints import complaints


def test_complaints(capfd):
    complaints(100, 60, 15, 5, 0)
    out1, err1 = capfd.readouterr()
    complaints(100, 70, 10, 5, 1)
    out2, err2 = capfd.readouterr()
    assert out1 == "95\n65\n45\n"
    assert out2 == "95\n175\n155\n"
