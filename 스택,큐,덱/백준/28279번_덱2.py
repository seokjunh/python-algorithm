import sys
from collections import deque

queue = deque()
for _ in range(int(input())):
    s = sys.stdin.readline().split()
    if s[0] == "1":
        queue.appendleft(int(s[1]))
    elif s[0] == "2":
        queue.append(int(s[1]))
    elif s[0] == "3":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif s[0] == "4":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif s[0] == "5":
        print(len(queue))
    elif s[0] == "6":
        if not queue:
            print(1)
        else:
            print(0)
    elif s[0] == "7":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s[0] == "8":
        if queue:
            print(queue[-1])
        else:
            print(-1)