cards = int(input())
cards_list = [int(card) for card in input().split()]

combinations = [[0 for j in range(cards)] for i in range(cards)]


def sabacchard_game(i, j):
    if i >= j:
        return 0
    elif i - j == 1:
        return max(cards_list[i], cards_list[j])

    if combinations[i][j]:
        return combinations[i][j]

    combinations[i][j] = max(
        max(cards_list[i], cards_list[j]) + sabacchard_game(i + 1, j - 1),
        cards_list[j] + sabacchard_game(i, j - 2),
        cards_list[i] + sabacchard_game(i + 2, j),
    )

    return combinations[i][j]


print(sabacchard_game(0, cards - 1))
