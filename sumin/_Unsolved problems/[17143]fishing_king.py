import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

shark_info = [list(map(int, input().split())) for _ in range(M)]
fishing_king = -1
graph = [[0] * M for _ in range(N)]
direc = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]

def fishing():
    for i in range(R):
        if graph[i][fishing_king]:
            return graph[i][fishing_king]


def movnig_shark(r, c, s, d, z): # 속력, 방향, 크기
    nr, nc, nd = r, c, d
     if d == 1: # Up (Row, Negative)
        if s < r:
            nr = r - s
        else:
            nr = (s - r) % (2*R - 2)
            if nr >= R:
                nr = 2*R - 2 - nr
            nd = 2 if int((s - r)/(R - 1)) % 2 == 0 else 1
    elif d == 2: # Down (Row, Positive)
        nr = (r + s) % (2*R - 2)
        if nr >= R:
            nr = 2*R - 2 - nr
        nd = 2 if int((r + s)/(R - 1)) % 2 == 0 else 1
    elif d == 3: # Right (Column, Positive)
        nc = (c + s) % (2*C - 2)
        if nc >= C:
            nc = 2*C - 2 - nc
        nd = 3 if int((c + s)/(C - 1)) % 2 == 0 else 4
    else: # d == 4, Left (Column, Negative)
        if s < c:
            nc = c - s
        else:
            nc = (s - c) % (2*C - 2)
            if nc >= C:
                nc = 2*C - 2 - nc
            nd = 3 if int((s - c)/(C - 1)) % 2 == 0 else 4
    return (nr, nc, s, nd, z)


def set_graph(point_lst):
    temp_lst = []
    for r, c, s, d, z in point_lst:
        temp_lst.append(movnig_shark(r, c, s, d, z))
        