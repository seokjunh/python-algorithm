N, M = map(int, input().split())

basket = [0] * N

for _ in range(M):
    i,j,k = map(int, input().split())
    while True:
        basket[i-1] = k
        if i == j:
            break
        i += 1
        
print(*basket)