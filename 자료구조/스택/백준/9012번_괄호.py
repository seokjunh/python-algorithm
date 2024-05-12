import sys
ps_list = [sys.stdin.readline() for _ in range(int(sys.stdin.readline()))]

for ps in ps_list:
    stack = []
    for i in ps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if not stack:
            print("YES")
        else:
            print("NO")