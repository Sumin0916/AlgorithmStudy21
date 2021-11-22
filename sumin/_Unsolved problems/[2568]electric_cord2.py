from bisect import bisect_left

N = int(input())
lines = [[0, 0]]+[list(map(int, input().split())) for _ in range(N)]
lines.sort()
print(lines)
dp = [0] * (N+1)
refrence = [-1*(1e10)]

for i in range(1, N+1):
    if refrence[-1] < lines[i][1]:
        refrence.append(lines[i][1])
        dp[i] = len(refrence) - 1
        ans = dp[i]
    else:
        dp[i] = bisect_left(refrence, lines[i][1])
        refrence[dp[i]] = lines[i][1]

res = set()
res2 = []
for i in range(N, 0, -1):
    if dp[i] == ans:
        res.add(lines[i][0])
        ans -= 1
    elif dp[i] != 0:
        res2.append(lines[i][0])

print(N-len(res))
res2.reverse()
for i in res2:
    print(i)
