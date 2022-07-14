def converter(degrees, scale):
    if scale == "celsius":
        return (degrees * 9 / 5) + 32
    elif scale == "fahrenheit":
        return (degrees - 32) * 5 / 9

