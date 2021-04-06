#전자레인지
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
Time = 0

while A<B:
    if A<0:
        Time+=C
    elif A==0:
        Time+=(D+E)
    elif A>0:
        Time+=E
    A+=1
print(Time)



