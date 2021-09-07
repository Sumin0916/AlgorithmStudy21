import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
point_lst = [list(map(int, input().split())) for _ in range(M)]
line_sum = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i != 0:
            line_sum[i][j] += line_sum[i-1][j]
        if j != 0:
            line_sum[i][j] += line_sum[i][j-1]
        line_sum[i][j] += array[i][j]
        if 0 < i < N and 0 < j < N:
            line_sum[i][j] -= array[0][0]

print(line_sum)
