N = int(input())

scores = sorted(list(map(int, input().split())))

M = scores[-1]

s = []
for i in range(len(scores)):
    s.append(scores[i]/M*100)

print(sum(s)/N)
