import sys

input = sys.stdin.readline
N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (N)
min_res = 1e8

def traveling(node, cost):
    global min_res, visited, ary
    if cost >= min_res:
        return
    if visited.count(False) == 0:
        print("helo")
        min_res = cost
        return
    n_lst = [x for x in range(N) if not visited[x] and ary[node][x] != 0]
    print(visited)
    if not n_lst:
        return
    for n in n_lst:
        visited[n] = True
        traveling(n, cost+ary[node][n])
        visited[n] = False

for i in range(N):
    traveling(i, 0)
print(min_res)


