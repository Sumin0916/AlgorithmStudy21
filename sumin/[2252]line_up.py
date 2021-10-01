import sys

input = sys.stdin.readline
line = []
dic = {}
N, M = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    if a in dic:
        
    elif b in dic:
    else:
        dic[a] = N
        dic[b] = N
