l = []
for i in range(9):
    n = int(input())
    l.append(n)
max_num = max(l)
print(max_num)
print(l.index(max_num)+1)

