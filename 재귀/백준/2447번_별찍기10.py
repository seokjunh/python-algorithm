N = int(input())

init = ["***", "* *", "***"]

def star(n, arr):
    if n == N:
        return arr
    
    temp = []

    for i in range(n):
        temp.append(arr[i] * 3)
    for i in range(n):
        temp.append(arr[i] + " " * n + arr[i])
    for i in range(n):
        temp.append(arr[i] * 3)

    return star(n*3,temp)

answer = star(3, init)

for i in answer:
    print(i)