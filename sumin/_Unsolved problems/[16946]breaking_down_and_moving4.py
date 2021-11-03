import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = list(list(map(int, list(input()))) for _ in range(N))

direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]


