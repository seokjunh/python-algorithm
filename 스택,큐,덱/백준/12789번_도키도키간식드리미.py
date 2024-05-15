N = int(input())
l = list(map(int, input().split()))

answer = "Nice"
min_num = 1
stack = []

for i in l:
    stack.append(i)
    while stack and stack[-1] == min_num:
        stack.pop()
        min_num += 1
    if len(stack) > 1 and stack[-1] > stack[-2]:
        answer = "Sad"
        break
if stack:
    answer = "Sad"
print(answer)
