def mmc(numbers):
    numbers.sort()
    num_a, num_b = numbers
    
    if num_a < 0 or num_b < 0:
        return
    
    elif num_a == 0 or num_b == 0:
        return 0
    
    elif num_b%num_a == 0:
        return num_b
    
    return num_a*num_b / (num_b%num_a)