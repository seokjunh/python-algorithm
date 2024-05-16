def solution(progresses, speeds):
    answer = []
    stack = []
    
    for i in range(len(progresses)):
        a = (100 - progresses[i]) // speeds[i]
        b = (100 - progresses[i]) % speeds[i]
        if b != 0:
            a += 1
        stack.append(a)

    cnt = 0
    max_day = stack[0]
    for i in range(len(progresses)):
        if stack[i] <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_day = stack[i]
    answer.append(cnt)

    return answer