def game_duration(start_hour, start_minutes, end_hour, end_minutes):
    """
    Calculate the duration of a game by
    - Converting the duration to minutes;
    - Checking if the duration is positive;
        - If not, add (24 * 60) minutes to the ending time;
    - Then, calculate the difference between the start and end time;
    """
    start_time = start_hour * 60 + start_minutes
    end_time = end_hour * 60 + end_minutes

    if start_time >= end_time:
        end_time += 24 * 60

    duration_in_hours = (end_time - start_time) // 60
    duration_in_min = (end_time - start_time) % 60

    return f"O jogo durou {duration_in_hours} horas e {duration_in_min} minutos."
