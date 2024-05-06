N, X = map(int, input().split())

s = list(map(int, input().split()))

for i in s:
    if i < X:
        print(i, end=' ')