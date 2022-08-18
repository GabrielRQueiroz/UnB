from codes.challenges.falling_circle import falling_circle


def test_falling_circle():
    #### CASE 1

    pattern = [
        [". O ."],
        [". . ."],
        ["X X X"],
    ]

    assert falling_circle(pattern) == [
        [". . ."],
        [". O ."],
        ["X X X"],
    ]

    #### CASE 2

    pattern = [
        [". O . O"],
        [". . . ."],
        ["X X X X"],
    ]

    assert falling_circle(pattern) == [
        [". . . ."],
        [". O . O"],
        ["X X X X"],
    ]

    #### CASE 3

    pattern = [
        ["O . . O"],
        [". O . ."],
        [". . . X"],
        ["X X X X"],
    ]

    assert falling_circle(pattern) == [
        [". . . ."],
        [". . . O"],
        ["O O . X"],
        ["X X X X"],
    ]

    #### CASE 4

    pattern = [
        ["O . . O"],
        ["O O . ."],
        [". . . X"],
        ["X X X X"],
    ]

    assert falling_circle(pattern) == [
        [". . . ."],
        ["O . . O"],
        ["O O . X"],
        ["X X X X"],
    ]

    #### CASE 5

    pattern = [
        ["O O . O"],
        ["O . . ."],
        [". O . ."],
        ["O . . ."],
        [". . . X"],
        ["X X X ."],
    ]

    assert falling_circle(pattern) == [
        [". . . ."],
        [". . . ."],
        ["O . . ."],
        ["O O . O"],
        ["O O . X"],
        ["X X X ."],
    ]
