import sys

input = sys.stdin.readline


def involution(num, power):
    res = 1
    while power:
        if power % 2:
            res *= num
        num *= num
        power // 2
    return res


X = 1000000007
expected_value = 0

M = int(input())

print(involution(2, 10))

    # if S % N:
    #     modular_inverse = involution(N, X-2) % X
    #     expected_value += S * modular_inverse % X
    # else:
    #     expected_value += S // N

