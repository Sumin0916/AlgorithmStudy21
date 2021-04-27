N,M = map(int,input().split())
nh=set()
ns=set()


for i in range(N):
    nh.add(input())


for i in range(M):
    ns.add(input())

l = list(nh&ns)
print(len(l))

for i in sorted(l):
    print(i)



