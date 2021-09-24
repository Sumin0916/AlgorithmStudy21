import sys
import copy
input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def matrix_product(a, b):
    res = [list(0 for _ in range(N)) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += a[i][k]*b[k][j]
    for i in range(N):
        for j in range(N):
            res[i][j] %= 1000
    return res


# ans = [list(0 for _ in range(N)) for _ in range(N)]
# for i in range(N):
    # ans[i][i] = 1

ans = copy.deepcopy(matrix)
C = 1
while C < B:
    if C % 2 == 1:
        ans = matrix_product(ans, matrix)
        C += 1
    else:
        if C * 2 < B:
            C *= 2
        else:
            break
        ans = matrix_product(ans, ans)

for i in range(B-C):
    ans = matrix_product(ans, matrix)

for i in range(N):
    for j in range(N):
        print(ans[i][j], end=" ")
    print()

