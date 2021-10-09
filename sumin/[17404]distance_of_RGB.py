import sys

input = sys.stdin.readline

N = int(input())
house_lst = list(list(map(int, input().split())) for _ in range(N))

for i in range(2, N-1):
    house_lst[i][0] = min(house_lst[i-1][1], house_lst[i-1][2]) + house_lst[i][0]
    house_lst[i][1] = min(house_lst[i-1][0], house_lst[i-1][2]) + house_lst[i][1]
    house_lst[i][2] = min(house_lst[i-1][0], house_lst[i-1][1]) + house_lst[i][2]
