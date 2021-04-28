n, m = map(int, input().split())

ice_box = [[0] * m for _ in range(n)]

for i in range(n):
    ice_box[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, - 1]


ice_cream_list = []

for i in range(n):
    for j in range(m):
        if ice_box[i][j] == 0:
            for fuck in ice_cream_list:
                if (i, j) not in fuck:
                    ice_cream_list.append({(i, j)})
           
            tmp_set = {(i, j)}
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if ice_box[nx][ny] == 0:
                        tmp_set.add((nx, ny))
            
            for element in ice_cream_list:
                cross = element & tmp_set
                if cross != None:
                    element = element | tmp_set

print(ice_cream_list)
    
