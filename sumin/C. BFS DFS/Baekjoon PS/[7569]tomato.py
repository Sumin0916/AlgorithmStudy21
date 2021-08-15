col, row, height = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(row)] for _ in range(height)]

print(box)