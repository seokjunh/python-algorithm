from collections import deque
N, K = map(int, input().split())

queue = deque([i+1 for i in range(N)])
answer = []
while True:
    if len(queue) == 0:
        print("<"+", ".join(answer)+">")
        break
    
    for _ in range(K-1):
        queue.append(queue.popleft())
    
    answer.append(str(queue.popleft()))

