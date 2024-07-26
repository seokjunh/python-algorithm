from collections import deque

def solution(info, edges):
    
    def build_tree(i,e):
        t = [[] for _ in range(len(i))]
        for edge in e:
            t[edge[0]].append(edge[1])
        return t
    
    tree = build_tree(info, edges)
    max_sheep = 0
    q = deque([(0,1,0,set())])
    
    while q:
        cur, sheep_cnt, wolf_cnt, visited = q.popleft()
        max_sheep = max(max_sheep, sheep_cnt)
        visited.update(tree[cur])
        
        for next_node in visited:
            if info[next_node]:
                if sheep_cnt != wolf_cnt + 1:
                    q.append((next_node, sheep_cnt, wolf_cnt+1, visited-{next_node}))
            else:
                q.append((next_node, sheep_cnt+1, wolf_cnt, visited-{next_node}))
    return max_sheep

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))