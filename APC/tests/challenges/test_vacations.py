from codes.challenges.vacations import vacations


def test_vacations():
    assert vacations("10/06", 70) == "Previsão de chegada: 21/08/2022"
    assert vacations("10/06", 141) == "Previsão de chegada: 02/11/2022"
    assert vacations("10/06", 199) == "Previsão de chegada: 30/12/2022"
    assert vacations("10/06", 200) == "Previsão de chegada: 01/01/2023"
    assert vacations("10/06", 561) == "Previsão de chegada: 02/01/2024"
