from triangle import area


def test_area():
    (triangle_area, square_area, circle_area, rect_area) = area(1, 2, 3)
    assert triangle_area == "1.500"
    assert circle_area == "9.870"
    assert square_area == "2.000"
    assert rect_area == "3.000"

