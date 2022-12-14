n = int(input())

reps_object = dict()


def fibonnaci(n):
    reps_object.update({n: reps_object.get(n, 0) + 1})

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


result = fibonnaci(n)

print(f"fibonacci({n}) = {result}.")
for reps in range(n + 1):
    if reps in reps_object:
        print(f"{reps_object[reps]} chamadas a fibonacci({reps}).")
    else:
        print(f"0 chamadas a fibonacci({reps}).")
