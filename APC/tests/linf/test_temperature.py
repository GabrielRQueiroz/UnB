from codes.linf.temperature import converter


def test_converter():
    assert converter(0, "celsius") == 32.0
    assert converter(32, "fahrenheit") == 0
    assert converter(24, "celsius") == 75.2
    assert converter(75.2, "fahrenheit") == 24
