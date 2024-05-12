def rotation(s):
    stack = []
    for i in range(len(s)):
        result = []
        for j in range(len(s)):
            result.append(s[(i+j) % len(s)])
        stack.append(result)
    return stack

def correct_bracket(i):
    stack = []
    for j in i:
        if j == "(" or j == "{" or j =="[":
            stack.append(j)
        elif j == ")" or j == "}" or j == "]":
            if not stack:
                return False
            else:
                if j == ")" and stack[-1] == "(":
                    stack.pop( ) 
                elif j == "]" and stack[-1] == "[":
                    stack.pop( ) 
                elif j == "}" and stack[-1] == "{":
                    stack.pop( )
    if stack:
        return False
    return True

def solution(s):
    cnt = 0
    rotated_list = rotation(s)
    for i in rotated_list:
        if correct_bracket(i):
            cnt += 1
    return cnt