cards = int(input())
cards_list = [int(card) for card in input().split()]


def sabacchard_game(cards_list):
    if len(cards_list) == 0:
        return 0

    elif len(cards_list) == 1:
        return cards_list[0]

    elif len(cards_list) == 2:
        return max(cards_list[0], cards_list[-1])
    
    else:
        best = max(*cards_list[:2:], *cards_list[-2::])

        cards_list.remove(min(*cards_list[:2:], *cards_list[-2::]))
        cards_list.remove(best)

        return best + sabacchard_game(cards_list)


print(sabacchard_game(cards_list))
