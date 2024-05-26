from collections import defaultdict
def solution(id_list, report, k):
    reporter = defaultdict(list)
    reported = defaultdict(int)

    for i in report:
        a,b = i.split()
        if b not in reporter[a]:
            reporter[a].append(b)
            reported[b] += 1

    answer = []
    for i in id_list:
        cnt = 0
        for j in range(len(reporter[i])):
            if reported[reporter[i][j]] >= k:
                cnt += 1
        answer.append(cnt)
    return answer