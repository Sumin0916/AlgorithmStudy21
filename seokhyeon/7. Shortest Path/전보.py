import heapq
import sys
input = sys.stdin.readline
INF = 987654321
# 도시 개수, 통로 개수, 메시지를 보내고자 하는 도시
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    # 특정 도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며, 메시지가 전달되는 시간은 z (x -> y: O, y -> x: X)
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []
heapq.heappush(q, (0, c))
distance[c] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt = 0
time = 0
for j in range(1, n + 1):
    if distance[j] == INF or j == c:
        continue
    else:
        cnt += 1
        time = max(time, distance[j])

print(cnt, end= " ")
print(time)
