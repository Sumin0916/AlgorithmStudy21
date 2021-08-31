import sys

input = sys.stdin.readline


# def cain_calendar(month, day, g_month, g_day):
    

# year 를 10으로 나누면 3, 12로 나누면 9
# 3, 13, 23, 33, 43, 54...
# 9, 21, 33, 45 ...


for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    if m < n:
        cain_calendar(m, n, x, y)
    elif m > n:
        cain_calendar(n, m, y, x)
    else:
        if x != y:
            print(-1)
        else:
            print(x)
# 11 13 6 5