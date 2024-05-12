def solution(N, stages):
    answer = {}
    n = len(stages)
    for i in range(1, N+1):
        if i in stages:
            answer[i] = stages.count(i) / n
            n -= stages.count(i)
        else:
            answer[i] = 0
    print(answer)
    return sorted(answer, key=lambda x:answer[x] ,reverse=True)