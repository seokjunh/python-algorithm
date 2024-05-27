N, M = map(int, input().split())

l = sorted(list(map(int, input().split())))

answer = []
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            current_num = l[i]+l[j]+l[k]
            if  current_num <= M:
                answer.append(current_num)
                
print(max(answer))