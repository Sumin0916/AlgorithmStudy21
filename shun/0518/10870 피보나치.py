F = int(input())
n=[0,1]

for i in range(2,F+1):
    num = n[i-1] + n[i-2]
    n.append(num)
print(n[F])
