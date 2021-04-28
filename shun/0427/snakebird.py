N,L = map(int,input().split())
h=list(map(int,input().split()))
h.sort()
res=L

for i in range(N):
    if res>=h[i]:
        res +=1

print(res)

