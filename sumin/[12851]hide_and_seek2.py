import sys

sys.setrecursionlimit(100000)

def hide_and_seek(point, time):
    if dp[point][0] < time:
        return
    elif dp[point][0] == time:
        dp[point][1] += 1
    elif dp[point][0] > time:
        dp[point][0] = time
        dp[point][1] = 1
    if point == K:
        return
    elif point > K:
        hide_and_seek(point-1, time+1)
    else:
        hide_and_seek(point+1, time+1)
        if point > 0:
            hide_and_seek(point-1, time+1)
        if point < 70000:
            hide_and_seek(point*2, time+1)
    

N, K = map(int, input().split())
dp = [[200000, 0] for _ in range(200000)]

hide_and_seek(N, 0)
print(dp[K][0])
print(dp[K][1])
    