def find(num, parent):
    if num == parent[num]:
        return num
    return find(parent[num], parent)

def union(a, b):
    n1 = find(a, parent)
    n2 = find(b, parent)
    if n1 > n2:
        parent[n1] = n2
    else:
        parent[n2] = n1


direc = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
N, M = map(int, input().split())
parent = [x for x in range(N*M)]
graph = [list(input()) for _ in range(N)]
ans_set = set()

for i in range(N*M):
    row = i // M
    col = i % M
    dr, dc = direc[graph[row][col]]
    direc_i = i+(M*dr)+dc
    union(i, direc_i)

for i in range(N*M):
    row = i // M
    col = i % M
    graph[row][col] = parent[i]

for i in graph:
    print(*i)





