from codes.questionnaires.reduce_matrix import reduce_matrix


def test_reduce_matrix():

    #### CASE 1

    matrix = [
        [5, 5, 7, 1],
        [2, 3, 1, 0],
        [7, 6, 8, 4],
        [4, 9, 3, 2],
    ]

    assert reduce_matrix(matrix, 2) == [
        [5, 7],
        [9, 8],
    ]

    #### CASE 2

    matrix = [
        [1, 2, 3, 4, 5, 6],
        [8, 9, 10, 12, 1, 3],
        [19, 3, 0, 1, 2, 1],
        [7, 8, 4, 3, 2, 9],
        [7, 4, 8, 9, 10, 2],
        [6, 4, 12, 13, 2, 8],
    ]

    assert reduce_matrix(matrix, 3) == [
        [19, 12],
        [12, 13],
    ]

    #### CASE 3

    matrix = [
        [439, 427, 155, 786, 256, 989],
        [354, 9, 119, 735, 141, 857],
    ]

    assert reduce_matrix(matrix, 2) == [[439, 786, 989]]
