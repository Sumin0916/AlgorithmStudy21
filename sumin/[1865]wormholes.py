import sys

input = sys.stdin.readline

T = int(input())
INF = 10000000001


def bellmanford(visited, graph, N, start):
    distance = [INF] * (N+2)
    distance[start] = 0
    for i in range(1, N+2):
        if distance[i] != INF:
            for u, t in graph[i]:
                if distance[i] + t < distance[u]:
                    distance[u] = distance[i] + t
    for i in range(1, N+2):
        for u, t in graph[i]:
             if distance[i] + t < distance[u]:
                    return True
    return False



for _ in range(T):
    N, M, W = map(int, input().split())
    graph = [list() for _ in range(N+2)]
    visited = [False] * (N+2)
    for i in range(1, N+1):
        graph[N+1].append([i, 0])
        graph[i].append([N+1, 0])
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for _ in range(W):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])
    res = bellmanford(visited, graph, N+1, N+1)
    if res:
        output = "YES"
    else:
        output = "NO"
    print(output)