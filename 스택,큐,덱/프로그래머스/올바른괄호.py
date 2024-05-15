def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[0] == ")":
                return False
            else:
                if stack[-1] != s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
    if len(stack) == 0:
        return True
    return False