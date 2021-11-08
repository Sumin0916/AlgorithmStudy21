def find(num, parent):
    if num == parent[num]:
        return num
    return find(parent[num], parent)

def union(a, b):
    n1 = find(a, parent)
    n2 = find(b, parent)
    if n1 > n2:
        parent[n1] = n2
        return n2
    elif n1 < n2:
        parent[n2] = n1
        return n1
    return False

direc = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
N, M = map(int, input().split())
parent = [x for x in range(N*M)]
graph = [list(input()) for _ in range(N)]
ans_set = set()
set_graph = [[0]*M for _ in range(N)]

for i in range(N*M):
    row = i // M
    col = i % M
    set_graph[row][col] = i

while True:
    is_change = False
    for i in range(N):
        for j in range(M):
            dr, dc = direc[graph[i][j]]
            nr, nc = i+dr, j+dc
            tmp = union(set_graph[i][j], set_graph[nr][nc])
            if tmp is not False:
                set_graph[i][j] = tmp
                set_graph[nr][nc] = tmp
                is_change = True
    if not is_change:
        break


for i in set_graph:
    print(*i)





