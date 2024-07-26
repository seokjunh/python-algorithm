from collections import deque

def bfs(m,s,e):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    q = deque([s])
    distance = {s:0}
    while q:
        cur = q.popleft()
        if cur == e:
            return directions[cur]
        for dx, dy in directions:
            nx, ny = cur[0] + dx, cur[1] + dy
            if 0 <= nx < len(m) and 0 <= ny < len(m[0]) and m[nx][ny] != "X":
                if (nx, ny) not in distance:
                    q.append((nx,ny))
                    distance[(nx,ny)] = distance[cur] + 1
def solution(maps:list) -> int:
    for i, row in enumerate(maps):
        for j, ceil in enumerate(row):
            if ceil == "S":
                start = (i,j)
            if ceil == "L":
                lever = (i,j)
            if ceil == "E":
                end = (i,j)
    time_to_lever = bfs(maps, start, lever)
    if time_to_lever == -1:
        return -1
    time_to_end = bfs(maps, lever, end)
    if time_to_end == -1:
        return -1
    return time_to_lever + time_to_end

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))