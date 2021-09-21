from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
chicken_lst = []
house_lst = []
min_res = 1000000000


def cal_chicken_distance(srow, scol):
    visited = [list(False for _ in range(N)) for _ in range(N)]
    queufrom collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
chicken_lst = []
house_lst = []
min_res = 1000000000

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
chicken_lst = []
house_lst = []
min_res = 1000000000


def cal_chicken_distance(srow, scol):
    visited = [list(False for _ in range(N)) for _ in range(N)]
    queue = from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
chicken_lst = []
house_lst = []
min_res = 1000000000


def cal_chicken_distance(srow, scol):
    visited = [list(False for _ in range(N)) for _ in range(N)]
    queue = deque()
    queue.append([srow, scol])
    visited[srow][scol] = True
deque()
    queue.append([srow, scol])
    visited[srow][scol] = True

def cal_chicken_distance(srow, scol):
    visited = [list(False for _ in range(N)) for _ in range(N)]
    queue = deque()
    queue.append([srow, scol])
    visited[srow][scol] = True
e = deque()
    queue.append([srow, scol])
    visited[srow][scol] = True

    while queue:
        row, col = queue.popleft()
        for r, c in direc:
            nr = row + r
            nc = col + c
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if graph[nr][nc] == 2:
                    return abs(srow - nr) + abs(scol - nc)
                visited[nr][nc] = True
                queue.append([nr, nc])


def select_chicken_house(order, count):
    global min_res
    res = 0
    if count == M:
        for r, c in house_lst:
            res += cal_chicken_distance(r, c)
        min_res = min(min_res, res)
        return
    for i in range(order, l_chicken):
        r, c = chicken_lst[i]
        graph[r][c] = 2
        select_chicken_house(order, l_chicken)
        graph[r][c] = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_lst.append([i, j])
        elif graph[i][j] == 2:
            chicken_lst.append([i, j])
            graph[i][j] = 0

l_chicken = len(chicken_lsselect_chicken_house(0, 0)

print(chicken_lst)
print(min_res)
