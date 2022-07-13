from codes.questionnaires.flow import flow


def test_flow():
    assert flow(("SIM", "SIM")) == [
        "O programa funciona?",
        "Você entende o que fez?",
        "Ótimo. Então não mexe!",
    ]
    assert flow(("SIM", "NÃO", "SIM")) == [
        "O programa funciona?",
        "Você entende o que fez?",
        "Já foi na tutoria?",
        "Choremos!",
    ]
