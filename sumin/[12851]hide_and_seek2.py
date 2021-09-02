import sys

sys.setrecursionlimit(10000)

n, k = map(int, input().split())
res_num = 0
mem = [100001 for _ in range(200001)]


def seek(now, goal, time):
    global min_res, res_num, mem
    if not (0 <= now <= 200000):
        return
    if time > mem[now]:
        return
    if now == goal:
        if time <= mem[now]:
            mem[now] = time
            res_num = 1
        else:
            res_num += 1
        mem[now] = time

    elif now > goal:
        seek(now-1, goal, time+1)

    else:
        seek(now-1, goal, time+1)
        seek(now+1, goal, time+1)
        seek(now*2, goal, time+1)


seek(n, k, 0)
print(mem[k])
print(res_num)
