def solution(dirs):
    answer = set()
    x,y = 0,0
    for i in dirs:
        nx,ny = x,y
        if i == "U":
            ny += 1
        elif i == "D":
            ny -= 1
        elif i == "R":
            nx += 1
        elif i == "L":
            nx -= 1
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((nx,ny,x,y))
            answer.add((x,y,nx,ny))
            x,y = nx,ny
    return len(answer)/2    