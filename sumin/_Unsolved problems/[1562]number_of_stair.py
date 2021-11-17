N = int(input())

start = 1000000000
ans = 0

while True:
    if start >= 10000000000:
        break
    s_num = str(start)
    ans += 1
    for i in range(1, 10):
        if abs(int(s_num[i])-int(s_num[i-1])) != 1:
            ans -= 1
            break
    ans %= 1000000000
    start += 1

print(ans)