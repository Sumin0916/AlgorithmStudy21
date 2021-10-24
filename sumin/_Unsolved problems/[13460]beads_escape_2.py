import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
red = []
blue = []

for i in range(N):
    temp = list(input().rstrip())
    for j in range(M):
        if temp[j] == "R":
            red = [i, j]
        elif temp[j] == "B":
            blue = [i, j]
    graph.append(temp)


def up_tilte(red, blue):
    global graph, N, M
    red_row, red_col = red
    blue_row, blue_col = blue
    for i in range(red_row-1, -1, -1):
        if graph[i][red_col] == "#":
            n_red_row = i+1
            break
        elif graph[i][red_col] == "O":
            if red_col == blue_col:
                if red_row > blue_row:
                    return "FAIL"
            return "GOAL"
    for i in range(blue_row-1, -1, -1):
        if graph[i][blue_col] == "#":
            n_blue_row = i+1
            break
    if n_red_row == n_blue_row:
        if red_row < blue_row:
            n_blue_row += 1
        else:
            n_red_row += 1
    new_red = [n_red_row, red_col]
    new_blue = [n_blue_row, blue_col]
    return [new_red, new_blue]


def down_tilte(red, blue):
    global graph, N, M
    red_row, red_col = red
    blue_row, blue_col = blue
    for i in range(red_row+1, N):
        if graph[i][red_col] == "#":
            n_red_row = i-1
            break
        elif graph[i][red_col] == "O":
            if red_col == blue_col:
                if red_row < blue_row:
                    return "FAIL"
            return "GOAL"
    for i in range(blue_row+1, N):
        if graph[i][blue_col] == "#":
            n_blue_row = i-1
            break
    if n_red_row == n_blue_row:
        if red_row > blue_row:
            n_blue_row -= 1
        else:
            n_red_row -= 1
    new_red = [n_red_row, red_col]
    new_blue = [n_blue_row, blue_col]
    return [new_red, new_blue]


def left_tilte(red, blue):
    global graph, N, M
    red_row, red_col = red
    blue_row, blue_col = blue
    for i in range(red_col-1, -1, -1):
        if graph[red_row][i] == "#":
            n_red_col = i+1
            break
        elif graph[red_row][i] == "O":
            if red_row == blue_row:
                if red_col > blue_col:
                    return "FAIL"
            return "GOAL"
    for i in range(blue_col-1, -1, -1):
        if graph[blue_row][i] == "#":
            n_blue_col = i+1
            break
    if n_red_col == n_blue_col:
        if red_col < blue_col:
            n_blue_col += 1
        else:
            n_red_col += 1
    new_red = [red_row, n_red_col]
    new_blue = [blue_row, n_blue_col]
    return [new_red, new_blue]


def right_tilte(red, blue):
    global graph, N, M
    red_row, red_col = red
    blue_row, blue_col = blue
    for i in range(red_col+1, N):
        if graph[red_row][i] == "#":
            n_red_col = i-1
            break
        elif graph[red_row][i] == "O":
            if red_row == blue_row:
                if red_col < blue_col:
                    return "FAIL"
            return "GOAL"
    for i in range(blue_col+1, N):
        if graph[blue_row][i] == "#":
            n_blue_col = i-1
            break
    if n_red_col == n_blue_col:
        if red_col < blue_col:
            n_red_col -= 1
        else:
            n_blue_col -= 1
    new_red = [red_row, n_red_col]
    new_blue = [blue_row, n_blue_col]
    return [new_red, new_blue]


def BFS(graph):
    global red, blue
    count =  0
    queue = deque()
    queue.append([red, blue])
    visited = [list(False for _ in range(M)) for _ in range(N)]
    visited[red[0]][red[1]] = True
    for _ in range(10):
        print(queue)
        count += 1
        temp = deque()
        while queue:
            red_lst, blue_lst = queue.popleft()
            temp_lst = []
            temp_lst.append(up_tilte(red_lst, blue_lst))
            temp_lst.append(down_tilte(red_lst, blue_lst))
            temp_lst.append(left_tilte(red_lst, blue_lst))
            temp_lst.append(right_tilte(red_lst, blue_lst))
            print(temp_lst)
            for res in temp_lst:
                if res == "GOAL":
                    return count
                elif res != "FAIL" and not visited[res[0][0]][res[0][1]]:
                    print("??!")
                    visited[res[0][0]][res[0][1]] = True
                    temp.append(res)
        if not temp:
            return -1
        queue = temp
    return -1

print(BFS(graph))
