"""
음료수 얼려 먹기
"""

def dfs_search(x,y, array, visited):
    if array[y][x] == 0:
        array[y][x] = 1
        visited.append([x, y])

    if y+1 <= len(array) - 1:
        if array[y+1][x] == 0:
            dfs_search(x, y+1, array, visited)

    if x+1 <= len(array[0]) - 1:
        if array[y][x+1] == 0:
            dfs_search(x+1, y, array, visited)

    else:
        p = visited.pop()
        if len(visited) == 0:
            return
        dfs_search(p[0], p[1], array, visited)
# dfs 알고리즘을 완벽하게 구현하지 못했다...

row, column = map(int, input().split())
ice_mold = []

for _ in range(row):
    tmp = input()
    tmp_lst = []
    for __ in tmp:
        if __ == "0":
            tmp_lst.append(0)
        else:
            tmp_lst.append(1)

    ice_mold.append(tmp_lst)

ice_cream = 0

for i in range(row):
    for j in range(column):
        if ice_mold[i][j] == 0:
            print(i, j)
            visited_mem = []
            dfs_search(j, i, ice_mold, visited_mem)
            ice_cream += 1
print(ice_mold)

print(ice_cream)