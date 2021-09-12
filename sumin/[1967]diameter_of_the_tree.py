import sys

input = sys.stdin.readline

n = int(input())
visited = [list(False for _ in range(n+1)) for _ in range(n+1)]
res = -1


def dfs():
