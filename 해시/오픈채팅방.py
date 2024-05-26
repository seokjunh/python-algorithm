def solution(record):
    answer = []
    record_dict = {}
    for i in record:
        l = i.split()
        if l[0] == "Enter" or l[0] == "Change":
            record_dict[l[1]] = l[2]
    for i in record:
        l = i.split()
        if l[0] == "Enter":
            answer.append("%s님이 들어왔습니다." %record_dict[l[1]])
        elif l[0] == "Leave":
            answer.append("%s님이 나갔습니다." %record_dict[l[1]])
            
    return answer