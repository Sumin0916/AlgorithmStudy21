N = int(input())
a=[0,1]

for i in range(2,N+1):
    num = a[i-1]+a[i-2]
    a.append(num)
print(a[N]*2 + (a[N]+a[N-1])*2)
