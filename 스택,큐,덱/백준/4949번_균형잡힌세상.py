while True:
    answer = "yes"
    n = input()
    stack = []
    if n == ".":
        break
    for i in n:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack:
                answer = "no"
                break
            else:
                if stack.pop() != "(":
                    answer = "no"
                    break
        elif i == "]":
            if not stack:
                answer = "no"
                break
            else:
                if stack.pop() != "[":
                    answer = "no"
                    break
        else:
            continue
    if stack:
        answer = "no"
    print(answer)
