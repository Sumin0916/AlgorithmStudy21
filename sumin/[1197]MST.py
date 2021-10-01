import sys

input = sys.stdin.readline
INF = 1e13
v, e = map(int, input().split())
graph = [list(0 for _ in range(v)) for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    


