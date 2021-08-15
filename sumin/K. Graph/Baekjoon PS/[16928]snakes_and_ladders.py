nladder, nsnakes = map(int, input().split())
board = [x for x in range(101)]
for _ in range(nladder):
    x, y = map(int, input().split())
    board[x] = y
for _ in range(nsnakes):
    u, v = map(int, input().split())
    board[u] = v

