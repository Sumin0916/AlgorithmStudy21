import sys
from collections import deque

input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()


def one_time_spread(queue):
    new_queue = deque()
    while queue:
        row, col = queue.popleft()
        new_queue.append([row, col])
        count = 0
        for r, c in direc:
            nr = r + row
            nc = c + col
            if 0 <= nr < R and 0 <= nc < C and not room[nr][nc] != -1:
                count += 1
                room[nr][nc] += room[row][col]//5
                new_queue.append([nr, nc])
        room[row][col] -= (room[row][col]//5) * count
    return new_queue


def air_purifier(row1, row2):
    queue = deque()
    queue.extend(room[row1][1:C-1])
    for i in range(row1, -1, -1):
        queue.append(room[i][C-1])
    queue.extend(room[0][C-2:0:-1])
    for i in range(row1):
        queue.append(room[0][i])
    print(queue)


air_purifier(2, 3)

