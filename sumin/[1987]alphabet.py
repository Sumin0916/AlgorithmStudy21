import sys

input = sys.stdin.readline
alpha_len = 26
SNUM = ord("A")
visited = [False] * alpha_len
direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
res = 0
R, C = map(int, input().split())
graph = [list(map(ord, list(input().rstrip()))) for _ in range(R)]
visited[graph[0][0] - SNUM] = True


def dfs_search(sr, sc):
    global res
    print(sr, sc)
    for r, c in direc:
        nr, nc = sr + r, sc + c
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[graph[nr][nc] - SNUM]:
                if res < nr + nc:
                    visited[graph[nr][nc] - SNUM] = True
                    res = nr + nc
                    dfs_search(nr, nc)
                    visited[graph[nr][nc] - SNUM] = False


dfs_search(0, 0)
print(res + 1)
