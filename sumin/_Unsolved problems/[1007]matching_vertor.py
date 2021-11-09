import sys
from itertools import permutations

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ans = 1e13
    N = int(input())
    p_lst = [list(map(int, input().split())) for _ in range(N)]
    per1 = list(permutations([x for x in range(N)], 2)) # n_P_2
    for i, j in per1:
        x1, y1 = p_lst[i]
        x2, y2 = p_lst[j]
        per2 = list(permutations([x for x in range(N) if not (x == i or x == j) ], 2))
        for m, n in per2:
            x3, y3 = p_lst[m]
            x4, y4 = p_lst[n]
            print(i, j, m, n)
            vec1 = (x1-x2, y1-y2)
            vec2 = (x3-x4, y3-y4)
            added_vec = (vec1[0]+vec2[0], vec1[1]+vec2[1])
            ans = min(ans, (((added_vec[0])**2)+((added_vec[1])**2))**(0.5))

    print(ans)
