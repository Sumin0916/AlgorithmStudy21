import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(map(ord, list(input())))
s.pop()
res = 0
dn = 2*n
want_hash = 0
for i in range(1, dn+1, 2):
    want_hash += 73 * (2 ** (i-1))
    want_hash += 79 * (2 ** i)
want_hash += 73 * (2 ** (dn))
new_hash = 0
for i in range(1, dn+1, 2):
    new_hash += s[i-1] * (2 ** (i-1))
    new_hash += s[i] * (2 ** i)
if new_hash == want_hash:
    res += 1
for i in range(dn+1, m-(dn)):
    new_hash = ((new_hash - s[i-dn]) // 2) + s[i] * (2 ** i)
    if new_hash == want_hash:
        res += 1
print(res)