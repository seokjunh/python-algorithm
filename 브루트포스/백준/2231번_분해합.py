N = int(input())

for i in range(1,N+1):
    num = i + sum(map(int, str(i)))
    if num == N:
        print(i)
        break
else:
    print(0)