reps = int(input("Quantas vezes repetir?\n> "))


def consecutive_and_sum(reps):
    for rep in range(reps):
        num_a, num_b = map(int, input("Valores:\n> ").split(" "))
        total = 0

        for consecutive in range(num_b):
            print(num_a, end=" ")
            total += num_a
            num_a += 1

        print(f"\n{total}")


consecutive_and_sum(reps)
