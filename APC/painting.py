def round_up(number):
    return round(number + (44.999999999 / 90))


def paint_price(aera):
    liters_needed = (aera / 6) * 1.1  # 1.1 are the extra 10%
    """
    Prices per liters of paint
    Note: 1 liter = 6 m²
    Note: 5 cans = 1 gallon => A gallon is cheaper than 5 cans
    """
    gallon_price = 80
    can_price = 25

    only_gallons = f"{(round_up(liters_needed / 18) * gallon_price):.2f} R$"
    only_cans = f"{(round_up(liters_needed / 3.6) * can_price):.2f} R$"

    """
    Mixed purchase proportions
    First we buy the gallons, then the cans (always in full cans)
    """
    best_gallons = liters_needed // 18
    best_cans = (liters_needed % best_gallons) / 3.6

    mixed_price = f"{((best_gallons * gallon_price) + (round_up(best_cans) * can_price)):.2f} R$"

    return (only_gallons, only_cans, mixed_price)
