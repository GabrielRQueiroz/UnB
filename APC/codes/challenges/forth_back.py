def forth_back(number):
    if number == 0:
        print(number)
        return

    acc = ""

    for i in range(number):
        acc += f"{i+1}"
        print(acc)

    for i in range(number, 0, -1):
        print(acc)
        acc = acc.replace(f"{i}", "")

    # for i in range(number - 1, 0, -1):
    #     acc = acc.replace(f"{i+1}", "")
    #     print(acc)
