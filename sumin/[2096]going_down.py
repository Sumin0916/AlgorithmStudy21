import sys

input = sys.stdin.readline

N = int(input())
INF = 1000000
ladder = [list(map(int, input().split())) for _ in range(N)]
max_dp = [0] * N
min_dp = [INF] * N
ind_lst = [[0, 1], [0, 1, 2], [1, 2]]
max_dp[0] = max(ladder[0])
min_dp[0] = min(ladder[0])

def recursive(floor, index):
    if floor == N:
        return
    if max_dp[floor-1] + ladder[floor][index] >= max_dp[floor]:
        
    if min_dp[floor-1] + ladder[floor][index] <= min_dp[floor]:
        
    return