from pythonds.basic.stack import Stack

plate_stack = Stack()

while True:
    plate_weight = int(input())

    if plate_weight == 0:
        break
    
    plate_stack.push(plate_weight)

if len(plate_stack) > 0:
    wanted_plate = int(input())

    plates_removed = 0
    weight_lifted = 0

    for i in range(len(plate_stack)-1, -1, -1):
        weight_lifted += plate_stack[i]
        plates_removed += 1
        print(f"Peso retirado: {plate_stack[i]}")
        
        if wanted_plate == plate_stack.peek():
            break
        else:
            plate_stack.pop()

    print(f"Anilhas retiradas: {plates_removed}")
    print(f"Peso total movimentado: {weight_lifted}")