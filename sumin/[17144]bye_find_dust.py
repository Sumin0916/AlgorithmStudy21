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


def clockwise_direc(row, col):
    if room[row][col] == -1:
        print(row, col)
        return
    print(row, col)
    if col == 0 and row > 0:
        room[row][col] = room[row-1][col]
        clockwise_direc(row-1, col)
    if row == 0 and col < C-1:
        room[row][col] = room[row][col+1]
        clockwise_direc(row, col+1)
    if col == C-1 and row < air_row[0]:
        room[row][col] = room[row+1][col]
        clockwise_direc(row+1, col)
    if row == air_row[0] and col > 0:
        room[row][col] = room[row][col-1]
        clockwise_direc(row, col-1)


air_row = []

for i in range(R):
    if room[i][0] == -1:
        air_row.append(i)
    if len(air_row) == 2:
        break

clockwise_direc(air_row[0]-1, 0)
room[air_row[0]][1] = 0
for i in room:
    print(i)

