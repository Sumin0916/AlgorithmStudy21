import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    dif = abs(m-n)
    if m > n:
        res = n
        tx, ty = y, y
        
    elif m < n:
        res = m
        tx, ty = x, x 
    else:
        if x == y:
            print(x)
        else:
            print(-1)