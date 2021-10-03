import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def move_line_up(graph, row, col, num):
    if not(0 <= row < N):
        return
    if graph[row][col] == 0:
        graph[row][col] = num
        temp = num
    elif graph[row][col] == num:
        temp = graph[row][col]
        graph[row][col] = num
    move_line_up(graph, row-1, col, temp)


