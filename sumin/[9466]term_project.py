import sys

def find_parent(parent, node, cal, start):
    if node not in cal:
        cal.add(node)
    elif node == start:
        return node  # 성공적인 사이클
    else:
        return -1  # 엉뚱한 사이클
    if parent[node] != node:
        find_parent(parent, parent[node], cal, start)

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count = 0
    N = int(input())
    student = list(map(int, input().split()))
    student.insert(0, 0)
    non_team = set()
    for i in range(1, N+1):
        print(i, find_parent(student, i, set(), i))
