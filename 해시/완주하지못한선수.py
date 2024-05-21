def solution(participant, completion):
    particy_dict = {}
    for i in range(len(participant)):
        if participant[i] in particy_dict:
            particy_dict[participant[i]] += 1
        else:
            particy_dict[participant[i]] = 1
        
    for i in completion:
        if i in particy_dict:
            particy_dict[i] -= 1
            if particy_dict[i] == 0:
                del particy_dict[i]

    return list(particy_dict.keys())[0]

# 다른 풀이
# from collections import Counter
# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))