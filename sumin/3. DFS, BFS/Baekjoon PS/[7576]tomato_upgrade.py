import sys
from collections import deque
r = sys.stdin.readline


def aaaasdaf(M, N, box):
    # 좌우상하
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1

    while wow:
        days += 1
        for _ in range(len(wow)):
            x, y = wow.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    wow.append([nx, ny])

    for b in box:
        if 0 in b:
            return -1
    return days


M, N = map(int, r().split())
box, wow = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1:
            wow.append([i, j])
    box.append(row)


print(aaaasdaf(M, N, box))