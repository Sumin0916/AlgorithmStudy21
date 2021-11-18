import sys
from itertools import combinations

def ccw(x1, x2, x3, y1, y2, y3):
    func = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    if func > 0:
        return 1
    elif func < 0:
        return -1
    else:
        return 0

input = sys.stdin.readline

N = int(input())

lines = []
group_dict = dict()

for i in range(N):
    lines.append(list(map(int, input().split()))+[i])

line_combi = list(combinations(lines, 2))

for line1, line2 in line_combi:
    x1, x1, x2, y2, i1 = line1
    x3, y3, x4, y4, i2 = line2
    a1 = ccw(x1, x2, x3, y1, y2, y3)
    a2 = ccw(x1, x2, x4, y1, y2, y4)
    b1 = ccw(x3, x4, x1, y3, y4, y1)
    b2 = ccw(x3, x4, x2, y3, y4, y2)
    if a1*a2 <= 0 and b1*b2 <= 0:
        if i1 in group_dict:
            
