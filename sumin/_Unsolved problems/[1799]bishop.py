import sys

N = int(input())
board = list(list(map(int, input().split())) for _ in range(N))
ans = 0
BISHOP = -1

def can_place(row, col):
    for r, c in bishop_lst:
        if col != c and row != r:
            if abs((row-r)/(col-c)) == 1:
                return False
    return True


def simulator(order, cnt):
    global board, ans, bishop_lst
    for i in range(order, lst_len):
        row, col = can_place_lst[i]
        if can_place(row, col):
            bishop_lst.append([row, col])
            simulator(order+1, cnt+1)
            bishop_lst.pop()
        simulator(order+1, cnt)
    ans = max(ans, cnt)

can_place_lst = []
bishop_lst = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            can_place_lst.append([i, j])
lst_len = len(can_place_lst)
print(can_place_lst)
simulator(0, 0)
print(ans)

