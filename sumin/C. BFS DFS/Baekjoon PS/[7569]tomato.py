from collections import deque

col, row, height = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(row)] for _ in range(height)]


def corrupt(graph, height, row, col):
    direc = [(0, 1, 0), (0, -1, 0), (0, 0, 1),
             (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
    temp = [(h+hight, r+row, c+col) for h, r, c in direc if h]


def bfs_search(graph):
    queue = deque()
    day = -1
    for i in range(height):
        for j in range(row):
            for k in range(col):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
    while queue:
        temp = []
        day += 1
        now = queue.popleft()
        
        