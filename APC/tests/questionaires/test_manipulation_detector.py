from codes.questionnaires.manipulation_detector import manipulation_detector


def test_manipulation_detector():

    #### CASE 1

    enterpreneus = {
        0: [10, 6, 4, 7, 1],
        1: [2, 9, 5, 3, 8],
    }

    players = [1, 1, 2, 2, 1, 1, 2, 1, 1, 2]

    assert manipulation_detector(enterpreneus, players, 2) == [1, 2]

    #### CASE 2

    enterpreneus = {
        0: [6, 9, 1, 4, 10],
        1: [2, 8, 13, 12, 5, 3, 7, 11],
    }

    players = [2, 3, 2, 3, 3, 1, 4, 2, 3, 1, 2, 4, 2]

    assert manipulation_detector(enterpreneus, players, 2) == -1
