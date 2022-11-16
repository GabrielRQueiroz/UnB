class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.size() > 0:
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


schedule_entry = input().split()
ordered_queue = Queue()

for i in range(0, len(schedule_entry), 2):
    ordered_queue.enqueue({schedule_entry[i]: int(schedule_entry[i + 1])})

ordered_queue.items = sorted(ordered_queue.items, key=lambda x: list(x.values())[0], reverse=True)

finished_tasks = int(input())

for _ in range(finished_tasks):
    ordered_queue.dequeue()

print(f"Tamanho da fila: {ordered_queue.size()}")

for task_index in range(ordered_queue.size() - 1, -1, -1):
    print(
        f"Atividade: {list(ordered_queue.items[task_index].keys())[0]}, Prioridade: #{ list(ordered_queue.items[task_index].values())[0]}"
    )
