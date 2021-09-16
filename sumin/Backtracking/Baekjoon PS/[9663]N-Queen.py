N = int(input())
row = [0] * N
res = 0


def judge(num):
    for i in range(num):
        if row[num] == row[i] or abs(row[num] - row[i]) == num - i:
            return False
    return True


def recursive(num):
    global res
    if num == N:
        res += 1
    else:
        for i in range(N):
            row[num] = i
            if judge(num):
                recursive(num+1)


recursive(0)
print(res)
