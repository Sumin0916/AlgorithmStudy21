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
    for i in edge:
        a, b = i[1], i[2]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            weight += i[0]
    return weight

N = int(input())
planet_lst = list(list(map(int, input().split())) for _ in range(N))
parent = [x for x in range(N)]
weight = 0

for i in range(N):
    x1, y1, z1 = planet_lst[i]
    for j in range(i+1, N):
        x2, y2, z2 = planet_lst[j]
        a, b = i, j
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            weight += min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
print(weight)