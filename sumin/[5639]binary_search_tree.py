import sys

input = sys.stdin.readline

res = []
data = None
count = 0
while count <= 10000:
    try:
        res.append(int(input()))
    except EOFError:
        break
    count += 1

print(res)
