def manipulation_detector(enterpreneurs, players=[1], teams=1):
    enterpreneurs_picks = {}

    for enterpreneur in range(len(enterpreneurs)):
        enterpreneurs_picks[enterpreneur] = set()

        for picks in enterpreneurs[enterpreneur]:
            enterpreneurs_picks[enterpreneur].add(players[picks - 1])

    manipulators = []

    for enterpreneur in range(len(enterpreneurs_picks)):
        if len(enterpreneurs_picks[enterpreneur]) == teams:
            manipulators.append(enterpreneur + 1)

    return manipulators if manipulators else -1
