import sys
import copy
from collections import deque

input = sys.stdin.readline

T = int(input())
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(h, w, visited, key, graph):
    documemt = 0
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        print(queue)
        now_row, now_col = queue.popleft()
        for dr, dc in direc:
            nr, nc = dr+now_row, dc+now_col
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                tile_type = graph[nr][nc]
                if tile_type == "*":
                    continue
                if tile_type == ".":
                    queue.append([nr, nc])
                    visited[nr][nc] = 1
                elif tile_type == "$":
                    documemt += 1
                    queue.append([nr, nc])
                    visited[nr][nc] = 1
                elif "a" <= tile_type <= "z":
                    key.add(tile_type)
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
                    graph[nr][nc] = "."
                    return -1
                elif "A" <= tile_type <= "Z":
                    if tile_type in key:
                        queue.append([nr, nc])
                        visited[nr][nc] = 1
                        graph[nr][nc] = "."

    return documemt

for _ in range(T):
    h, w = map(int, input().split())
    h += 2
    w += 2
    init_visited = [[0 for _ in range(w)] for _ in range(h)]
    graph = [["." for _ in range(w)]]
    for i in range(h-2):
        graph.append(["."] + list(input().rstrip()) + ["."])
    graph.append(["." for _ in range(w)])
    key = input()
    if key == "0":
        key = set()
    else:
        key = set(list(key))
    ans = -1
    while ans == -1:
        visited = copy.deepcopy(init_visited)
        ans = bfs(h, w, visited, key, graph)
    print()
    for i in visited:
        print(*i)
    print()
    print(ans)

    

    