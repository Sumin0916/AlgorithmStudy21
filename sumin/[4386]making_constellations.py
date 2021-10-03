import sys

input = sys.stdin.readline

N = int(input())
star_dict = {}
for i in range(1, N+1):
    star_dict[i] = list(map(float, input().split()))
edge = []
lst = []


def combi(ind, cnt):
    if cnt == 2:
        print(lst)
        return
    for i in range(ind, N+1):
        lst.append(i)
        combi(ind+1, cnt+1)
        lst.pop()


combi(1, 0)

