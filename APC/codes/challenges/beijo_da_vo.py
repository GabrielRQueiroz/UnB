def prize(slices, winner, clients={"foo": 0}):
    cake_slices = [0] * slices
    cake_slices[winner] = 1

    for client in clients:
        choice = clients[client]
        prize = cake_slices.index(1)

        if choice == prize:
            return client
        else:
            del cake_slices[clients[client]]
            continue
