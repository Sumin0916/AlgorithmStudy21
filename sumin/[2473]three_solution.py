N = int(input())
sol = list(map(int, input().split()))
sol.sort()

res = [1e10, []]
s = 0
e = N-1
m = (s+e)//2

while s <= m and m <= e:
    if s == m and m == e:
        break
    new_sol = abs(sol[s]+sol[m]+sol[e])
    if new_sol < res[0]:
        res[0] = new_sol
        res[1] = [sol[s], sol[m], sol[e]]
    if new_sol < 0:
        if m+1 == e:
            s += 1
        else:
            m += 1
            
    elif new_sol > 0:
        if m-1 == s:
            e -= 1
        else:
            m -= 1
    else:
        res[0] = 0
        res[1] = [sol[s], sol[m], sol[e]]

print(res[0])
print(*res[1])
