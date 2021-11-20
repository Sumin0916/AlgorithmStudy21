N = int(input())

dp = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(N+1)]

full = (1<<10)-1

for i in range(1, 10):
    dp[1][i][1<<i] = 1

for i in range(2, N+1):    
    for j in range(10):
        for k in range(full):
            if j == 0:
                dp[i][j][k|(1<<0)] = dp[i-1][1][k]
            elif j == 9:
                dp[i][j][k|(1<<9)] = dp[i-1][8][k]
            else:
                dp[i][j][k|(1<<j)] = dp[i-1][j-1][k] + dp[i-1][j+1][k]

ans = 0

for i in range(10):
    ans += dp[N][i][full]

print(ans)