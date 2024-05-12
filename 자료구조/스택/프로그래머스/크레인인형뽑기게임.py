def solution(board, moves):
    cnt = 0
    stack = []
    for i in moves:
        for j in board:
            if j[i-1] == 0:
                pass
            else:
                if not stack:
                    stack.append(j[i-1])
                    j[i-1] = 0
                    break
                else:
                    if stack[-1] == j[i-1]:
                        stack.pop()
                        cnt += 2
                        j[i-1] = 0
                        break
                    else:
                        stack.append(j[i-1])
                        j[i-1] = 0
                        break
    return cnt