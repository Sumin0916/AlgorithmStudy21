n = int(input())
data = list(input().split())

x = 1
y = 1

# for direction in data:
#     if direction == 'R':
#         if y >= 1 and y < n:
#             y += 1
#     elif direction == 'L':
#         if y > 1 and y <= n:
#             y -= 1
#     elif direction == 'U':
#         if x > 1 and x <= n:
#             x -= 1
#     elif direction == 'D':
#         if x >= 1 and x < n:
#             x += 1

# 깔끔히 정리하면

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in data:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
