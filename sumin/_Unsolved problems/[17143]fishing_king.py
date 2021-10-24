import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

shark_info = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    shark_info[i][0] -= 1
    shark_info[i][1] -= 1
fising_king = -1
graph = [list(False for _ in range(C)) for _ in range(R)]
res = 0
direc = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}  # 위, 아래, 오른쪽, 왼쪽

for r, c, s, d, z in shark_info:
    graph[r][c] = [s, d, z]


def fising(point):
    global graph
    for i in range(R):
        if graph[i][point]:
            temp = graph[i][point][2]
            graph[i][point] = 0
            print(temp)
            return temp
    return 0


def moving_shark():
    global shark_info, graph, direc, R, C
    temp_shark_info = []
    for r, c, s, d, z in shark_info:  # 속력, 이동방향, 크기
        graph[r][c] = False
        dr, dc = direc[d]
        dr = s*dr
        dc = s*dc
        if d == 1 or d == 2:
            s %= ((2 * R)-2)
        elif d == 3 or d == 4:
            s %= ((2 * C)-2)
        if r == 0 and d == 1:
            d = 2
        elif r == R-1 and d == 2:
            d = 1
        elif c == C-1 and d == 3:
            d = 4
        elif c == 0 and d == 4:
            d = 3
        nr, nc = r, c
        for _ in range(s):
            if d == 1:
                nr -= 1
                if nr - 1 < 0:
                    d = 2
            elif d == 2:
                nr += 1
                if nr + 1 >= R:
                    d = 1
            elif d == 3:
                nc += 1
                if nc + 1 >= C:
                    d = 4
            elif d == 4:
                nc -= 1
                if nc -1 < 0:
                    d = 3
        temp_shark_info.append([nr, nc, s, d, z])
    for r, c, s, d, z in temp_shark_info:
        if not graph[r][c]:
            graph[r][c] = [s, d, z]
        else:
            if graph[r][c][2] < z:
                graph[r][c] = [s, d, z]
    return temp_shark_info


while True:
    fising_king += 1
    if fising_king == C:
        break
    res += fising(fising_king)
    shark_info = moving_shark()
print(res)