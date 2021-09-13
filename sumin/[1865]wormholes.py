import sys

input = sys.stdin.readline

T = int(input())
INF = 10000001

for _ in range(T):
    N, M, W = map(int, input().split())
    graph = [list() for _ in range(N+1)]
    distance = []
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for _ in range(W):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])
