from math import pi


def area(a, b, c):
    triangle_area = f"{((a * c) / 2):.3f}"
    circle_area = f"{((pi * a) ** 2):.3f}"
    square_area = f"{(a * b):.3f}"
    rect_area = f"{(a * c):.3f}"

    return triangle_area, square_area, circle_area, rect_area
