T = int(input())
N = int(input())
a_ary = [0] + list(map(int, input().split()))
M = int(input())
b_ary = [0] + list(map(int, input().split()))
res = 0

for i in range(1, N+1):
    a_ary[i] += a_ary[i-1]
for i in range(1, M+1):
    b_ary[i] += b_ary[i-1]
print(a_ary)
for i in range(N+1):
    for j in range(i+1, N+1):
        s = a_ary[j] - a_ary[i]
        if s >= T:
            break
        for m in range(M+1):
            for n in range(m+1, M+1):
                s += b_ary[n] - b_ary[m]
                if s > T:
                    break
                elif s == T:
                    print(j, i, n, m)
                    res += 1
                    break

print(res)
