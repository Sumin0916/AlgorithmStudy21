from itertools import combinations

N, S = map(int, input().split())
ary = list(map(int, input().split()))

left_lst = ary[:N//2]
right_lst = ary[N//2:]
left_sum = [0] * (sum(left_lst) + 1)
right_sum = [0] * (sum(left_lst) + 1)

