from datetime import date as dt


def vacations(date, days_out):
    day, month = date.split("/")
    day = int(day)
    month = int(month)
    year = dt.today().year

    totalDays = (month * 30) + day + days_out

    day = ((totalDays) % 30) + 1
    month = (((totalDays // 30) - 1) % 12) + 1
    year += (totalDays - 30) // 360

    return f"Previsão de chegada: {day:02d}/{month:02d}/{year}"
