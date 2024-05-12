l = []
for _ in range(10):
    n = int(input())
    l.append(n % 42)
print(len(set(l)))