def define_greatest(greatest = 0, time=1, prev = []):
    if time > 10:
        print(f"-=-=-=-=-=-\nPrimeiro: {prev[0]}\nMaior: {greatest}\n-=-=-=-=-=-")
        return
    
    new_number = int(input())
    prev.append(new_number)
        
    if greatest > new_number:
        return define_greatest(greatest, time + 1, prev)
    else:
        return define_greatest(new_number, time + 1, prev)
    
define_greatest()