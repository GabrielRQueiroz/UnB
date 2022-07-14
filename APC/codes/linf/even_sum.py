def even_sum(number, total=0):
    if number == 0:
        return total

    if number < 0:
        return -1

    if number % 2 != 0:
        number -= 1

    total += number - 2

    return even_sum(number - 2, total)
