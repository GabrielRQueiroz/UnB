def fibonacci(num):
    if num < 1:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    # init = 1
    # acc = 1
    # for generations in range(num - 2):
    #     total = init + acc
    #     init = acc
    #     acc = total
    # return total


def factorial(num):
    for i in range(num - 1, 1, -1):
        num *= i

    return num


def fibofat(num):
    """
    Return the fibonacci number at the position represented by the input AND the input's factorial.
    - IF the fibonacci number is even, return the number from the previous position. 
    """
    fib = fibonacci(num)
    fac = factorial(num)
    
    if fib % 2 == 0:
        return f"{fib} {fac} {fibonacci(num-1)}"
        
    return f"{fib} {fac}"


