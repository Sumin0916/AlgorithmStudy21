import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()


def one_time_spread(queue):
    new_queue = deque()
    adder_lst = []
    subs_lst = []
    while queue:
        row, col = queue.popleft()
        new_queue.append([row, col])
        count = 0
        for r, c in direc:
            nr = r + row
            nc = c + col
            if 0 <= nr < R and 0 <= nc < C:
                if room[nr][nc] != -1:
                    count += 1
                    new_queue.append([nr, nc])
                    adder_lst.append([nr, nc, int(room[row][col]/5)])
        if count >= 1:
            subs_lst.append([row, col, (int(room[row][col]/5)) * count])
    for r, c, a in adder_lst:
        room[r][c] += a
    for r, c, s in subs_lst:
        room[r][c] -= s
    return new_queue


def clockwise_direc(row, col):
    if room[row][col] == -1:
        return
    if col == 0 and row > 0:
        room[row][col] = room[row-1][col]
        clockwise_direc(row-1, col)
    elif row == 0 and col < C-1:
        room[row][col] = room[row][col+1]
        clockwise_direc(row, col+1)
    elif col == C-1 and row < air_row[0]:
        room[row][col] = room[row+1][col]
        clockwise_direc(row+1, col)
    elif row == air_row[0] and col > 0:
        room[row][col] = room[row][col-1]
        clockwise_direc(row, col-1)


def reverse_clockwise(row, col):
    if room[row][col] == -1:
        return
    if col == 0 and row < R-1:
        room[row][col] = room[row+1][col]
        reverse_clockwise(row+1, col)
    elif row == R-1 and col < C-1:
        room[row][col] = room[row][col+1]
        reverse_clockwise(row, col+1)
    elif col == C-1 and row > air_row[1]:
        room[row][col] = room[row-1][col]
        reverse_clockwise(row-1, col)
    elif row == air_row[1] and col > 0:
        room[row][col] = room[row][col-1]
        reverse_clockwise(row, col-1)


air_row = []

for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            queue.append([i, j])
        elif room[i][j] == -1:
            air_row.append(i)


for _ in range(T):
    for i in room:
        print(i)
    print()
    queue = one_time_spread(queue)
    clockwise_direc(air_row[0]-1, 0)
    room[air_row[0]][1] = 0
    reverse_clockwise(air_row[1]+1, 0)
    room[air_row[1]][1] = 0

room[air_row[0]][0] = 0
room[air_row[1]][0] = 0
print(sum(list(map(sum, room))))


