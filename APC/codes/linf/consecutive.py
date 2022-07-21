def consecutive_and_sum(reps, num_a, num_b):
    for rep in range(reps):
        sequence = []
        total = 0

        for consecutive in range(num_b):
            sequence.append(num_a)
            total += num_a
            num_a += 1

        return f"{' '.join(str(num) for num in sequence)}\n{total}"
    
# In:
# 1
# 1 3
#
# Out:
# > 1 2 3
# > 6
