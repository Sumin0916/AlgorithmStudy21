*order, void = map(int, input().split())
len_order = len(order)
cost_table = [list(0 for _ in range(5)) for _ in range(5)]
cost_table[0] = [1e10, 2, 2, 2, 2]
INF = 1e10
for i in range(1, 5):
    cost_table[i][0] = 2
    for j in range(1, 5):
        if abs(i-j) == 0:
            cost_table[i][j] = 1
        elif abs(i-j) == 1 or abs(i-j) == 3:
            cost_table[i][j] = 3
        elif abs(i-j) == 2:
            cost_table[i][j] = 4

dp = [list(list(INF for _ in range(5)) for _ in range(5)) for _ in range(len_order)]

for i in range(1, len_order):
    num = order[i]
    for j in range(5):
        for k in range(5):
            if (j == num):
                for m in range(5):
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][cost_table[m][j]][k])
            elif (k == num):
                for m in range(5):
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][cost_table[m][k]])


print(min(cost_table[len_order-1][order[len_order-1]]))