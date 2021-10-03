import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def can_move(bead_point, visited):
    new_point = []
    rr, rc = bead_point[0][0], bead_point[0][1]
    br, bc = bead_point[1][0], bead_point[1][1]
    for i in range(4):
        nrr = dx[i] + rr
        nrc = dy[i] + rc
        nbr = dx[i] + br
        nbc = dy[i] + bc
        if 0 <= nrr < N and 0 <= nrc < M:
            if graph[nrr][nrc] == "O":
                return "GOAL"
            elif graph[nrr][nrc] == "#":
                nrr = rr
                nrc = rc
        if 0 <= nbr < N and 0 <= nbc < M:
            if graph[nbr][nbc] == "#":
                nbr = br
                nbc = bc
            if graph[nbr][nbc] == "O":
                continue
        if not (nrr == nbr and nrc == nbc):
            if not visited[nrr][nrc]:
                new_point.append([[nrr, nrc], [nbr, nbc]])
                visited[nrr][nrc] = True
    return new_point


def bfs_search(start_info):
    queue = deque()
    queue.append(start_info)
    visited = [list(False for _ in range(M)) for _ in range(N)]
    visited[start_info[0][0]][start_info[0][1]] = True
    count = 0
    while queue:
        print(queue)
        count += 1
        if count > 10:
            return -1
        temp_queue = deque()
        while queue:
            bead_info = queue.popleft()
            lst = can_move(bead_info, visited)
            if lst == "GOAL":
                return count
            temp_queue.extend(lst)
        queue = temp_queue
    for i in visited:
        print(*i)
    return -1


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
start_point = [None, None]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "B":
            start_point[1] = [i, j]
        elif graph[i][j] == "R":
            start_point[0] = [i, j]

print(bfs_search(start_point))

