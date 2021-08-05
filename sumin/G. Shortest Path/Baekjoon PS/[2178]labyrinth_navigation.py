n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]


def can_move(array, i, j):
    global n, m
    if 0 <= i < n and 0 <= j < m and array[i][j]:
        return [i, j]
    else:
        return False


def navigate(array):
    lst = array
    RIGHT, DOWN, UP, LEFT = 0, 1, 2, 3
    res = 1
    row, col = 0, 0
    mem = UP  # 이번 수행에서는 위로 올라가지 말라는 이야기
    haha = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while True:
        move = False
        if row == n-1 and col == m-1:
            return res
        direc = [can_move(lst, row, col+1),
                 can_move(lst, row+1, col),
                 can_move(lst, row-1, col),
                 can_move(lst, row, col-1)]

        for i in range(4):
            if i == mem:
                continue
            elif direc[i]:
                row, col = direc[i][0], direc[i][1]
                # print(i, row, col)
                res += 1
                move = True
                if i == 0:
                    mem = 3
                elif i == 1:
                    mem = 2
                elif i == 2:
                    mem = 1
                elif i == 3:
                    mem = 0
                break
        if not move:
            lst[row][col] = 0
            row += haha[mem][0]
            col += haha[mem][1]
            res -= 1
        # time.sleep(1)


def navigate_r(array):
    DOWN, RIGHT, UP, LEFT = 0, 1, 2, 3
    lst = array
    res = 1
    row, col = 0, 0
    mem = UP  # 이번 수행에서는 위로 올라가지 말라는 이야기
    haha = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while True:
        move = False
        if row == n-1 and col == m-1:
            return res
        direc = [can_move(lst, row+1, col),
                 can_move(lst, row, col+1),
                 can_move(lst, row-1, col),
                 can_move(lst, row, col-1)]

        for i in range(4):
            if i == mem:
                continue
            elif direc[i]:
                row, col = direc[i][0], direc[i][1]
                # print(i, row, col)
                res += 1
                move = True
                if i == 0:
                    mem = 2
                elif i == 1:
                    mem = 3
                elif i == 2:
                    mem = 0
                elif i == 3:
                    mem = 1
                break
        if not move:
            lst[row][col] = 0
            row += haha[mem][0]
            col += haha[mem][1]
            res -= 1
        # time.sleep(1)



print(min(navigate(maze), navigate_r(maze)))


