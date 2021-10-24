import sys
import heapq

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal(edge):
    weight = 0
    for i in range(E):
        if find_parent(parent, edge[i][1]) != find_parent(parent, edge[i][2]):
            union_parent(parent, edge[i][1], edge[i][2])
            weight += edge[i][0]
    return weight

def combi(ind, cnt):
    global edge, E
    if cnt == 2:
        if lst[0] != lst[1]:
            s1 = dic[lst[0]]
            s2 = dic[lst[1]]
            dis = min(abs(s1[0]-s2[0]), abs(s1[1]-s2[1]), abs(s1[2]-s2[2]))
            heapq.heappush(edge, [dis, lst[0], lst[1]])
            E += 1
        return
    for i in range(ind, N+1):
        lst.append(i)
        combi(ind+1, cnt+1)
        lst.pop()

N = int(input())
edge = []
lst = []
parent = [x for x in range(N+1)]
dic = {}
E = 0

for i in range(1, N+1):
    x, y, z = map(int, input().split())
    dic[i] = [x, y, z]
combi(1, 0)
print(kruskal(edge))
