n=int(input())
a=[0,1]
for i in range(2,n+1):
   num=a[i-1]+a[i-2]
   a.append(num)
print(a[n])
    