n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split())) # 한줄씩 받아서?
    min_num = data[0]
    for j in range(m):
        min_num = min(min_num, data[j])

    result = max(min_num, result)

print(result)


    