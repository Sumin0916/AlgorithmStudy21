graph = [list(map(int, list(input()))) for _ in range(9)]

def check_validity(row, col, num):
    for i in range(9):
        if i != col and graph[row][i] == num:
            return False
        if i != row and graph[i][col] == num:
            return False
    return True


def solve_sudoku(order, graph):
    if order > 81:
        return
    for i in range(order, 9*9):
        row = i // 9
        col = i % 9
        if graph[row][col] == 0:
            print(row, col)
            for c in range(1, 10):
                if check_validity(row, col, c):
                    graph[row][col] = c
                    solve_sudoku(i+1, graph)
                    graph[row][col] = 0
            return


solve_sudoku(0, graph)
print(graph)