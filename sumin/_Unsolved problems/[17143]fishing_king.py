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
    if d == 1: # Up
        s = s % ((R-1)*2)
    elif d == 2: # Down
        s = s % ((R-1)*2)
    elif d == 3: # Right
        s = s % ((C-1)*2)

    elif d == 4: # Left
        s = s % ((C-1)*2)
    return (r, c, s, d, z)


