n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 게임 맵 저장
game_map = [[0]*n for _ in range(m)]
for i in range(m):
    tmp = list(map(int, input().split()))
    game_map[i] = tmp

# 이동 방향 저장 0:북,1:동,2:남,3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 지나간 곳들 저장
remember_data = [(x, y)]

result = 0

while True:
    for i in range(4):
        tmp = (7 + d - i) % 4
        next_x = x + dx[tmp]
        next_y = y + dy[tmp]

        if game_map[next_x][next_y] == 0 and (next_x, next_y) not in remember_data:
            x = next_x
            y = next_y
            result += 1
            remember_data.append((x, y))
            d = tmp
            break

    if x != next_x or y != next_y:
        next_x = x - dx[d]
        next_y = y - dy[d]

        if game_map[next_x][next_y] == 1:
            break
        else:
            result += 1
            x = next_x
            y = next_y

print(result)
print(x, y)
print(next_x, next_y)
print(remember_data)
print(d)

        
    



