#1이 될 때까지
count = 0
N,K = map(int,input().split())

while True:

    if N == 1 :
        break

    if N % K == 0 :
        N/=K
        count+=1

    else:
        N -=1
        count +=1

print(count)