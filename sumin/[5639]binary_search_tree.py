import sys

input = sys.stdin.readline
res = []
data = None
while True:
    try:
        res.append(int(input()))
    except EOFError:
        break
print(res)
