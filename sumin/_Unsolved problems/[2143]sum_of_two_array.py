T = int(input())
N = int(input())
a_ary = list(map(int, input().split()))
M = int(input())
b_ary = list(map(int, input().split()))
res = 0

for i in range(1, N):
    a_ary[i] += a_ary[i-1]
for i in range(1, M):
    b_ary[i] += b_ary[i-1]


for i in range(N):

