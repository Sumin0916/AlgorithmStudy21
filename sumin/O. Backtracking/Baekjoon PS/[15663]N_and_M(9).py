import copy

n, m = list(map(int, input().split()))
s = sorted(list(map(int, input().split())))
res = []
mem = []


def back_tracking(st):
    if len(res) == m:
        print(' '.join(map(str, res)))
        mem.append(copy.deepcopy(res))
        return

    for i in range(len(s)):
        if i != st:
            res.append(s[i])
            back_tracking(i)
            res.pop()


back_tracking(-1)
