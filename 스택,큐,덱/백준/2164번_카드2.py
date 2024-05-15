from collections import deque

N = int(input())
queue = deque([i+1 for i in range(N)])

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    v = queue.popleft()
    queue.append(v)