import sys
from collections import deque

input = sys.stdin.readline
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())
graph = list(list(input()) for _ in range(N))


def moving_bids(direction, red_point, blue_point):
    dr, dc = direc[direction]
    red_row, red_col = red_point
    blue_row, blue_col = blue_point
    red_stat, blue_stat = True, True

    while red_stat or blue_stat:
        if red_stat:
            nred_row = red_row+dr
            nred_col = red_col+dc
            if 0<= nred_row < N and 0 <= nred_col < M and graph[nred_row][nred_col] != "#":
                if graph[nred_row][nred_col] == "O":
                    return "END"
                red_row = nred_row
                red_col = nred_col
            else:
                red_stat = False
        if blue_stat:
            nblue_row = blue_row+dr
            nblue_col = blue_col+dc
            if 0<= nblue_row < N and 0 <= nblue_col < M and graph[nblue_row][nblue_col] != "#":
                if graph[nblue_row][nblue_col] == "O":
                    return "RE"
                blue_row = nblue_row
                blue_col = nblue_col
            else:
                blue_stat = False

    if red_row == blue_row and red_col == blue_col:
        if red_point[0] == blue_point[0]:
            if red_point[1] > blue_point[1]:
                if direction == 2:
                    blue_col -= 1
                elif direction == 3:
                    red_col -= 1
            else:
                if direction == 2:
                    red_col -= 1
                elif direction == 3:
                    blue_col -= 1
        elif red_point[1] == blue_point[1]:
            if red_point[0] > blue_point[0]:
                if direction == 0:
                    blue_col -= 1
                elif direction == 1:
                    red_col -= 1
            else:
                if direction == 0:
                    red_col -= 1
                elif direction == 1:
                    blue_col -= 1

    return (red_row, red_col), (blue_row, blue_col)


def bfs():
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "R":
                red_point = (i, j)
            elif graph[i][j] == "B":
                blue_point = (i, j)
    point_queue = deque()
    point_queue.append((red_point, blue_point))

    while point_queue:
        count += 1
        while point_queue:
            red_point, blue_point = point_queue.popleft()
            for i in range(4):
                res = moving_bids(i, red_point, blue_point)
                if res == "END":
                    return count
                elif res == "RE":
                    pass
                else:
                    point_queue.append(tuple(res))

print(bfs())


