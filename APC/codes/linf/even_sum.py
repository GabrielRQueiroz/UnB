def even_sum(number, total = 0):
    if number == 0:
        print(total)
        return
    
    if number < 0:
        print(-1)
        return
        
    if number % 2 != 0:
        number -= 1
        
    total += number
        
    return even_sum(number-2, total)

number = int(input())-2

even_sum(number)