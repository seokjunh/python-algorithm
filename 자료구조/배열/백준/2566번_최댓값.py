max_num = 0
idx_1,idx_2 = 0,0

for i in range(9):
    l = list(map(int, input().split()))
    max_l = max(l)
    if max_l >= max_num:
        max_num = max_l
        idx_1 = i+1
        idx_2 = l.index(max_num)+1

print(max_num)
print(idx_1,idx_2)