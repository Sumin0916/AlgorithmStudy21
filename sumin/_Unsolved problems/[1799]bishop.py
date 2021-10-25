import sys


def put_it(row, col):
    global N, graph
    for i in range(1, row+1):
        if 0 <= col+i < N:
            if graph[row-i][col+i] == -1:
                return False
        if 0 <= col-i < N:
            if graph[row-i][col-i] == -1:
                return False
    for i in range(1, N-row):
        if 0 <= col+i < N:
            if graph[row+i][col+i] == -1:
                return False
        if 0 <= col-i < N:
            if graph[row+i][col-i] == -1:
                return False
    graph[row][col] = -1
    return True
    
def find_ans(len_place, ind, count):
    global graph, visited, res
    if ind == len_place:
        res = max(res, count)
        return
    for i in range(ind, len_place):
        if not visited[i]:
            row, col = placable[i] 
            visited[i] = True
            if put_it(row, col):
                graph[row][col] = -1
                count += 1
            find_ans(len_place, ind+1, count)
            graph[row][col] = 0
            visited[i] = False



N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
placable = []
res = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            placable.append([i, j])

len_place = len(placable)
visited = [False] * len_place
print(put_it(1, 1))
print(put_it(4, 4))