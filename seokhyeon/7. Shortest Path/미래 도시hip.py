import heapq
import sys
input = sys.stdin.readline
INF = 9876543210

# 노드 개수, 간선 개수 입력 받기
n, m  = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # a번 노드에서 b번 노드 가는 거 표시
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def short_cut(start, end):
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]

result = short_cut(1, k) + short_cut(k, x)

if result >= INF:
    print(-1)
else:
    print(result)