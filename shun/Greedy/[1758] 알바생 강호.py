N = int(input())
tip = []
for i in range(N):
    tip.append(int(input()))

tip.sort(reverse=True)

res = 0
for i in range(N):
    give = tip[i]-i
    if give<0:
        give=0
    res += give
print(res)