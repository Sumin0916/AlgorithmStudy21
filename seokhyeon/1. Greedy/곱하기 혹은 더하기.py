n = input()

result = 0

for i in n:
    # 0 이거나 1 이거나 저장값이 0이면
    if int(i) == 0 or int(i) == 1 or result == 0:
        result += int(i)
    else:
        result *= int(i)

print(result)

