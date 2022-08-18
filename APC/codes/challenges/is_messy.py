def is_messy(original="A B C", movements=["A D 0"]):
    original = original.split(" ")

    modified = original.copy()

    for command in movements:
        commands = command.split(" ")
        toy = commands[0]
        toy_pos = modified.index(toy)

        if commands[2] == "0":
            continue

        if commands[1] == "D":
            modified.remove(toy)
            if toy_pos + int(commands[2]) < len(original):
                modified.insert(toy_pos + int(commands[2]), toy)

            else:
                modified.append(toy)

        elif commands[1] == "E":
            modified.remove(toy)
            if toy_pos - int(commands[2]) > 0:
                modified.insert(toy_pos - int(commands[2]), toy)
            else:
                modified.insert(0, toy)

    messes = 0

    for item in range(len(original)):
        if original[item] != modified[item]:
            messes += 1

    return messes
