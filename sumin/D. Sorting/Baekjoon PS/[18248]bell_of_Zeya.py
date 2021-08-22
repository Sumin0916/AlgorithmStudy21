n, m = map(int, input().split())
a = set()
b = set()
res = "YES"
for _ in range(n):
    lst = list(map(int, input().split()))
    for i in range(m):
        if lst[i] == 1 and i not in a:
            a.add(i)
        elif lst[i] == 0 and i not in b:
            b.add(i)
        if lst[i] == 1 and i in b or lst[i] == 0 and i in a:
            res = "NO"
            break
    if res == "NO":
        break

print(res)
