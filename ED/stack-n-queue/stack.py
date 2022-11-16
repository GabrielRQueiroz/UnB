class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


plate_stack = Stack()

while True:
    plate_weight = int(input())

    if plate_weight == 0:
        break

    plate_stack.push(plate_weight)

if plate_stack.size() > 0:
    wanted_plate = int(input())

    plates_removed = 0
    weight_lifted = 0

    for i in range(plate_stack.size() - 1, -1, -1):
        weight_lifted += plate_stack.peek()
        plates_removed += 1

        print(f"Peso retirado: {plate_stack.peek()}")

        if wanted_plate == plate_stack.peek():
            break
        else:
            plate_stack.pop()

    print(f"Anilhas retiradas: {plates_removed}")
    print(f"Peso total movimentado: {weight_lifted}")
