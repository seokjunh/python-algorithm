def insert(tree, node, parent_idx):
    idx, x, y = node
    (p_x, p_y), left, right = tree[parent_idx]

    if p_x < x:
        if right != 0:
            insert(tree, node, right)
        else:
            tree[parent_idx][2] = idx
            tree[idx] = [(x,y),0,0]
    else:
        if left != 0:
            insert(tree, node, left)
        else:
            tree[parent_idx][1] = idx
            tree[idx] = [(x,y),0,0]

def preOrder(tree, node_idx):
    path = []

    if node_idx == 0:
        return path
    
    path.append(node_idx)
    path += preOrder(tree, tree[node_idx][1])
    path += preOrder(tree, tree[node_idx][2])

    return path

def postOrder(tree, node_idx):
    path = []

    if node_idx == 0:
        return path
    
    path += postOrder(tree, tree[node_idx][1])
    path += postOrder(tree, tree[node_idx][2])
    path.append(node_idx)

    return path

def solution(nodeinfo:list) -> list:
    sorted_nodeinfo = []

    for idx, [x,y] in enumerate(nodeinfo,1):
        sorted_nodeinfo.append([idx,x,y])
    
    sorted_nodeinfo.sort(key=lambda x: x[2])

    tree = {}
    root_idx, root_x, root_y = sorted_nodeinfo.pop()
    tree[root_idx] = [(root_x,root_y),0,0]

    while sorted_nodeinfo:
        node = sorted_nodeinfo.pop()
        insert(tree, node, root_idx)
    
    answer = [preOrder(tree, root_idx), postOrder(tree, root_idx)]
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))