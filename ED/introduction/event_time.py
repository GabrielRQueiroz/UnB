"""
Crie um programa que calcule a duração total de um evento sabendo o dia, hora, minutos e segundos para as datas inicial e final do mesmo.
"""

FIRST_INPUT = "5 08:12:23"
SECOND_INPUT = "9 06:13:23"


def event_time(starting_date: str, ending_date: str) -> str or list:
    duration = list()

    try:
        first_day, first_time = starting_date.split()
        last_day, last_time = ending_date.split()

        if (
            len(first_time.split(":")[0]) != len(last_time.split(":")[0])
            or len(first_time.split(":")[1]) != len(last_time.split(":")[1])
            or len(first_time.split(":")[2]) != len(last_time.split(":")[2])
        ):
            return "Data inválida!"

        first_day = int(first_day)
        last_day = int(last_day)

        first_hour, first_minute, first_second = list(map(int, first_time.split(":")))
        last_hour, last_minute, last_second = list(map(int, last_time.split(":")))

        if (
            first_day > last_day
            or first_hour > 24
            or last_hour > 24
            or first_minute > 60
            or last_minute > 60
            or first_second > 60
            or last_second > 60
        ):
            return "Data inválida!"

        if first_hour > last_hour:
            last_day -= 1
            last_hour += 24

        if first_minute > last_minute:
            last_hour -= 1
            last_minute += 60

        if first_second > last_second:
            last_minute -= 1
            last_second += 60

        duration.append(f"{last_day - first_day} dia(s)")
        duration.append(f"{last_hour - first_hour} hora(s)")
        duration.append(f"{last_minute - first_minute} minuto(s)")
        duration.append(f"{last_second - first_second} segundo(s)")

        return duration

    except:
        return "Data inválida!"


def event_time_second_try(starting_date: str, ending_date: str) -> str or list:
    duration = list()

    try:
        first_day, first_time = starting_date.split()
        last_day, last_time = ending_date.split()

        if (
            len(first_time.split(":")[0]) != len(last_time.split(":")[0])
            or len(first_time.split(":")[1]) != len(last_time.split(":")[1])
            or len(first_time.split(":")[2]) != len(last_time.split(":")[2])
        ):
            return "Data inválida!"

        first_day = int(first_day)
        last_day = int(last_day)

        first_hour, first_minute, first_second = list(map(int, first_time.split(":")))
        last_hour, last_minute, last_second = list(map(int, last_time.split(":")))

        if (
            first_day > 30
            or first_day < 0
            or last_day > 30
            or last_day < 0
            or first_hour >= 24
            or first_hour < 0
            or last_hour >= 24
            or last_hour < 0
            or first_minute >= 60
            or first_minute < 0
            or last_minute >= 60
            or last_minute < 0
            or first_second >= 60
            or first_second < 0
            or last_second >= 60
            or last_second < 0
        ):
            return "Data inválida!"

        total_seconds = (
            (last_day - first_day) * 86400
            + (last_hour - first_hour) * 3600
            + (last_minute - first_minute) * 60
            + (last_second - first_second)
        )

        if total_seconds < 0:
            return "Data inválida!"

        total_days = total_seconds // 86400
        total_seconds %= 86400

        total_hours = total_seconds // 3600
        total_seconds %= 3600

        total_minutes = total_seconds // 60
        total_seconds %= 60

        duration.append(f"{total_days} dia(s)")
        duration.append(f"{total_hours} hora(s)")
        duration.append(f"{total_minutes} minuto(s)")
        duration.append(f"{total_seconds} segundo(s)")

        return duration

    except:
        return "Data inválida!"


for _ in event_time(FIRST_INPUT, SECOND_INPUT):
    print(_)
