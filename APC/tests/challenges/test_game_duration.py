from codes.challenges.game_duration import game_duration


def test_game_duration():
    assert game_duration(9, 0, 10, 0) == "O jogo durou 1 horas e 0 minutos."
    assert game_duration(7, 10, 8, 9) == "O jogo durou 0 horas e 59 minutos."
    assert game_duration(7, 7, 7, 7) == "O jogo durou 24 horas e 0 minutos."
    assert game_duration(7, 7, 7, 6) == "O jogo durou 23 horas e 59 minutos."
