import sys

input = sys.stdin.readline
dp = [list(1e10 for _ in range(3)) for _ in range(2)]
N = int(input())

for _ in range(N):
    