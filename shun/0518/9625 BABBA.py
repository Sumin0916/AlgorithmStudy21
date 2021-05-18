k = int(input())
a=[1,0]
b=[0,1]

for i in range(2,k+1):
    num = a[i-1] + a[i-2]
    a.append(num)
    num2 = b[i-1] + b[i-2]
    b.append(num2)
print(a[k],b[k])