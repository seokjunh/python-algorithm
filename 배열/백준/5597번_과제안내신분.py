students = [0] * 30

for _ in range(28):
    n = int(input())
    students[n-1] += 1

for i in range(len(students)):
    if students[i] == 0:
        print(i+1)
        students[i] += 1
