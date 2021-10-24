import sys

input = sys.stdin.readline

T = int(input())


def permutation(ind, cnt, lst):
    global res
    if cnt == 2:
        print(lst)
        a = point[lst[0]]
        b = point[lst[1]]
        cal = (((a[0]-b[0])**2) + ((a[1]-b[1])**2)) ** (0.5)
        res = min(res, cal)
        print(res)
        return
    for i in range(len_point):
        if len(lst) > 0 and lst[0] == i:
            continue
        lst.append(i)
        permutation(ind+1, cnt+1, lst)
        lst.pop()


def combi(ind, cnt):
    if cnt == 


for _ in range(T):
    N = int(input())
    point = [list(map(int, input().split())) for _ in range(N)]
    res = 200000 * 21
    len_point = len(point)
    permutation(0, 0, [])
    print(res)
