from collections import deque
NINF = -1
n, m = map(int, input().split())
barrack = [list(map(int, input().split())) for _ in range(n)]


def can_move(graph, level_graph, row, col, stat):
    direc = [(1, 0, 0), (0, 1, 0), (0, -1, 0), (-1, 0, 0),
             (2, 0, 1), (0, 2, 1), (0, -2, 1), (-2, 0, 1)]
    now_level = graph[row][col]
    res = []
    if stat:
        temp = [(row+r, col+c, 1) for r, c, s in direc[:4] if 0 <= row+r <= n-1 and 0 <= col+c <= m-1]
    else:
        temp = [(row+r, col+c, s) for r, c, s in direc if 0 <= row+r <= n-1 and 0 <= col+c <= m-1]
    for r, c, s in temp:
        original_future_level = graph[r][c]
        future_level = level_graph[r][c]
        if future_level == NINF:
            if now_level < original_future_level:
                level_graph[r][c] = original_future_level
            else:
                level_graph[r][c] = now_level
            res.append((r, c, s))
        else:
            if future_level > now_level:
                level_graph[r][c] = now_level
                res.append((r, c, s))
    return res


def bfs_search(graph):
    if n == 1 and m == 1:
        return graph[n-1][m-1]
    level_map = [[NINF for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        row, col, stat = queue.popleft()
        if not (row == n-1 and col == m-1):
            lst = can_move(graph, level_map, row, col, stat)
            if lst:
                queue.extend(lst)
    for r in level_map:
        print(r)
    return level_map[n-1][m-1]


print(bfs_search(barrack))
