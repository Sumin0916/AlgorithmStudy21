T = int(input())
N = int(input())
a_ary = [0] + list(map(int, input().split()))
M = int(input())
b_ary = [0] + list(map(int, input().split()))
res = 0

for i in range(1, N):
    a_ary[i] += a_ary[i-1]
for i in range(1, M):
    b_ary[i] += b_ary[i-1]


for i in range(1, N):
    for j in range(0, i):
        a = a_ary[i] - a_ary[j]
        for m in range(1, N):
            for n in range(0, m):
                b = b_ary[m] - b_ary[n]
                if a + b == T:
                    res += 1

print(res)


