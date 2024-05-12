n = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    a,b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            n[a+j][b+i] = 1


answer = 0
for i in n:
    answer += i.count(1)
print(answer)