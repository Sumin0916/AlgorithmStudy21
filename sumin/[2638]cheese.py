import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)
time = 0

N, M = map(int, input().split())
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
graph = [list(map(int, input().split())) for _ in range(N)]

def modify_vacuum_stat(row, col, want_stat):
    if not (0 <= row < N and 0 <= col < M):
        return
    if graph[row][col] == 1:
        return
    if graph[row][col] == want_stat:
        return
    else:
        graph[row][col] = want_stat
    modify_vacuum_stat(row+1, col, want_stat)
    modify_vacuum_stat(row-1, col, want_stat)
    modify_vacuum_stat(row, col+1, want_stat)
    modify_vacuum_stat(row, col-1, want_stat)


def is_malting(row, col):
    count = 0
    for r, c in direc:
        nr = row + r
        nc = col + c
        if 0 <= nr < N and 0 <= nc < M:
            if graph[nr][nc] == 0:
                count += 1
    if count >= 2:
        return True
    else:
        return False


def find_none_vacuum(row, col):
    for r, c in direc:
        nr = row + r
        nc = col + c
        if 0 <= nr < N and 0 <= nc < M:
            if graph[nr][nc] == -1:
                modify_vacuum_stat(nr, nc, 0)
                return True
    return False


def malting_cheese(lst):
    remain_lst = []
    malting_lst = []
    for row, col in lst:
        if is_malting(row, col):
            malting_lst.append([row, col])
        else:
            remain_lst.append([row, col])

    for row, col in malting_lst:
        graph[row][col] = 0
        find_none_vacuum(row, col)
    return remain_lst

cheese_lst = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            modify_vacuum_stat(i, j, -1)
        else:
            cheese_lst.append([i, j])

modify_vacuum_stat(0, 0, 0)

while cheese_lst:
    cheese_lst = malting_cheese(cheese_lst)
    time += 1
    for i in graph:
        print(*i)
    print()

print(time)


