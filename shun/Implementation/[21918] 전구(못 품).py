N,M = map(int,input().split(''))

bulbs=list(map(int,input().split('')))
cnt=[0]*(N+1)
for i in range(M):
    a,b,c=map(int,input().split(''))
    if a==1:
        bulbs[b-1]==1
    elif a==2:
        for j in range(b-1,c):
            if bulbs[j] == 0:
                bulbs[j] =1
            elif bulbs[j] ==1:
                bulbs[j] =0
    elif a==3:
        bulbs[b-1:c]==0
    elif a==4:
        bulbs[b-1:c]==1
    
print(N)
        

