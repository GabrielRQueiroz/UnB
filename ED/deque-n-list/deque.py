from collections import deque

list_size = int(input())
items = list(map(int, input().split()))
sublist_size = int(input())
indexes_deque = deque([index for index in range(0, sublist_size)])
sliding_window = list()

for i in range(sublist_size, list_size + 1):
    sliding_window.append(str(max(items[slice(indexes_deque.popleft(), i)])))
    indexes_deque.append(i)

print("  ".join(sliding_window))
