n, m = map(int, input().split())

ice_box = [[0] * m for _ in range(n)]

for i in range(n):
    ice_box[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, - 1]


ice_cream_list = [{(-1, -1)}]

# 1차 약팔이 과정
for i in range(n):
    for j in range(m):
        cnt = 0
        if ice_box[i][j] == 0:
            for fuck in ice_cream_list:
                if (i, j) not in fuck:
                    cnt += 1
            if cnt == len(ice_cream_list):
                ice_cream_list.append({(i, j)})
           
            tmp_set = {(i, j)}
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if ice_box[nx][ny] == 0:
                        tmp_set.add((nx, ny))
            
            for q in range(len(ice_cream_list)):
                if ice_cream_list[q] & tmp_set != set():
                    ice_cream_list[q] = ice_cream_list[q] | tmp_set

print(ice_cream_list)

result_list = []

# 2차 약팔이 과정, 중복 되있는 거 제거
for v in range(len(ice_cream_list)):
    if ice_cream_list[v] not in result_list and ice_cream_list[v] != {(-1, -1)}:
        result_list.append(ice_cream_list[v])

print(result_list)
print(len(result_list))
real_result_list = []

# 3차 약팔이 과정, 두 요소간 교집합이 공집합이 되도록
for a in range(len(result_list)):
    proof = 0
    for b in range(len(result_list)):
        if result_list[a] & result_list[b] != set() and a != b:
            proof += 1
            new_set = result_list[a] | result_list[b]
            if new_set == result_list[a] or new_set == result_list[b]:
                if new_set not in real_result_list:
                    real_result_list.append(new_set)
            else:
                if new_set not in real_result_list:
                    real_result_list.append(new_set)
    if proof == 0 and result_list[a] not in real_result_list:
        real_result_list.append(result_list[a])
        
            

print(real_result_list)
print(len(real_result_list))


    



