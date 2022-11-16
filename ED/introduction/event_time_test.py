from event_time import event_time, event_time_second_try


def test_insert_time():
    assert event_time("5 08:12:23", "9 06:13:23") == [
        "3 dia(s)",
        "22 hora(s)",
        "1 minuto(s)",
        "0 segundo(s)",
    ]

    assert event_time("5 07:15:23", "9 06:13:23") == [
        "3 dia(s)",
        "22 hora(s)",
        "58 minuto(s)",
        "0 segundo(s)",
    ]

    assert event_time("5 08:12:23", "5 08:12:23") == [
        "0 dia(s)",
        "0 hora(s)",
        "0 minuto(s)",
        "0 segundo(s)",
    ]

    assert event_time("5 02:02:02", "7 2:2:2") == "Data inválida!"

    assert event_time("5 07:15:23", "9 06:61:23") == "Data inválida!"

    assert event_time("5 08:12:23", "4 06:13:23") == "Data inválida!"

    assert event_time("5 08:12:23:500", "4 06:13:23:500") == "Data inválida!"

    assert event_time("5 08:12:23 12", "4 06:13:23 12") == "Data inválida!"

    assert event_time("abc", "deg") == "Data inválida!"


def test_insert_time_second_try():
    assert event_time_second_try("5 08:12:23", "9 06:13:23") == [
        "3 dia(s)",
        "22 hora(s)",
        "1 minuto(s)",
        "0 segundo(s)",
    ]

    assert event_time_second_try("5 07:15:23", "9 06:13:23") == [
        "3 dia(s)",
        "22 hora(s)",
        "58 minuto(s)",
        "0 segundo(s)",
    ]

    assert event_time_second_try("5 08:12:23", "5 08:12:23") == [
        "0 dia(s)",
        "0 hora(s)",
        "0 minuto(s)",
        "0 segundo(s)",
    ]

    assert event_time_second_try("5 08:12:23", "15 23:59:59") == [
        "10 dia(s)",
        "15 hora(s)",
        "47 minuto(s)",
        "36 segundo(s)",
    ]

    assert event_time_second_try("5 08:12:59", "15 00:00:00") == [
        "9 dia(s)",
        "15 hora(s)",
        "47 minuto(s)",
        "1 segundo(s)",
    ]

    assert event_time_second_try("5 08:12:23", "15 -1:00:00") == "Data inválida!"

    # assert event_time_second_try("5 07:15:23", "9 06:61:23") == "Data inválida!"

    assert event_time_second_try("5 08:12:23", "4 06:13:23") == "Data inválida!"

    assert event_time_second_try("5 08:12:23:500", "4 06:13:23:500") == "Data inválida!"

    assert event_time_second_try("5 08:12:23 12", "4 06:13:23 12") == "Data inválida!"

    assert event_time_second_try("abc", "deg") == "Data inválida!"
