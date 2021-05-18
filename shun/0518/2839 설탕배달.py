n = int(input())
a=0

while n>=0:
    if n % 5 ==0:
        a += (n //5)   
        print(a)
        break
    n -=3
    a +=1
else:
    print(-1)