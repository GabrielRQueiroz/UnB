numbers = input().split(" ")
numbers[0] = int(numbers[0])
numbers[1] = int(numbers[1])
numbers.sort()

def mmc(num_a, num_b):
    if num_a < 0 or num_b < 0:
        return
    
    elif num_a == 0 or num_b == 0:
        return 0
    
    elif num_b%num_a == 0:
        return num_b
    
    return num_a*num_b / (num_b%num_a)
    
print(mmc(numbers[0], numbers[1]))