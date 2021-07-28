n, m = map(int, input().split())
tetrominos = [
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]
]


def rotate(m):
    ret = [[0] * 4 for _ in range(4)]

    for r in range(4):
        for c in range(4):
            ret[c][3-r] = m[r][c]
    return ret

def flip(block):
    for i in range(2):
        for j in range(4):
            block[j][i], block[j][3 - i] = block[j][3 - i], block[j][i]


def get_score(ary, block, n, m, i, j):
    copy_ary = [[0, 0, 0, 0] for _ in range(4)]
    sumi = 0
    ti = i - 3
    for a in range(4):
        tj = j - 3
        for b in range(4):
            if 0 <= ti < n and 0 <= tj < m:
                copy_ary[a][b] = ary[ti][tj]
            tj += 1
        ti += 1
    for a in range(4):
        for b in range(4):
            if block[a][b] == 1 and copy_ary[a][b] != 0:
                sumi += copy_ary[a][b]
    return sumi


score = -1
array = [list(map(int, input().split())) for _ in range(n)]
# 0~2 대칭 x 1은 회전 X
for i in range(n):
    for j in range(m):
        for b in range(5):
            block = tetrominos[b]
            for r in range(4):
                block = rotate(block)
                for f in range(2):
                    flip(block)
                    temp = get_score(array, block, n, m, i, j)
                    if temp > score:
                        score = temp

print(score)
