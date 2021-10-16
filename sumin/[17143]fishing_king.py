R, C, M = map(int, input().split())

shark_info = [list(map(int, input().split())) for _ in range(M)]
fising_king = -1
graph = [list(0 for _ in range(C)) for _ in range(R)]
res = 0
direc = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}


for r, c, s, d, z in shark_info:
    graph[r-1][c-1] = [s, d, z]

def fising(point):
    global graph
    for i in range(R):
        if graph[i][point] != 0:
            temp = graph[i][point][2]
            graph[i][point] = 0
            return temp
    return 0


def moving_shark():
    global shark_info, graph, direc, R, C
    temp_shark_info = []
    for r, c, s, d, z in shark_info:  # 속력, 이동방향, 크기
        graph[r][c] = 0
        dr, dc = direc[d]
        dr = r + s*dr
        dc = c + s*dc
        nr, nc = r+dr, c+dc
        if nr < 0:
            nr = R - (abs(nr) % (R-1))
            d = 2
        elif nr >= R:
            nr = nr % (R-1)
            d = 1
        elif nc < 0:
            nc = C - (abs(nc) % (C-1))
            d = 3
        elif nc >= C:
            nr = nr % (C-1)
            d = 4
        temp_shark_info.append([r, c, s, d, z])
    for r, c, s, d, z in temp_shark_info:
        if graph[r][c] == 0:
            graph[r][c] = [s, d, z]
        else:
            if graph[r][c][2] < z:
                graph[r][c] = [s, d, z]


while fising_king < C:
    fising_king += 1
    res += fising(fising_king)
