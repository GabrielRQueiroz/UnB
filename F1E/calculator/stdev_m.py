from numpy import sqrt, std


def stdev_m(values: list = []):
    length = len(values)
    stdev = std(values)

    return stdev / sqrt(length - 1)
