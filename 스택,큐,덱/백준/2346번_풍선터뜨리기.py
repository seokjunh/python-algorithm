from collections import deque

N = int(input())
queue = deque(enumerate(map(int, input().split())))

for i in range(N):
    idx, tmp = queue.popleft()
    print(idx+1, end=" ")
    if tmp > 0:
        queue.rotate(-(tmp-1)) #왼쪽으로 회전
    else:
        queue.rotate(-tmp) #오른쪽으로 회전
