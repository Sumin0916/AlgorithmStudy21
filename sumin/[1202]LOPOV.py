import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewely = []
res = 0

for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewely, [-v, m])

bag = []
for _ in range(K):
    heapq.heappush(bag, int(input()))

v, m = heapq.heappop(jewely)
v *= -1
while bag and jewely:
    space = heapq.heappop(bag)
    print(v, m, space, bag, jewely)
    if m <= space:
        res += v
    v, m = heapq.heappop(jewely)
    v *= -1
print(res)
