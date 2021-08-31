n = int(input())
result = 4

for i in range(int(n**0.5), int((n//2)**0.5)-1, -1):
    a = n - i*i
    if a == 0: 
        result=1
        break
    for j in range(int(a**0.5), int((a//2)**0.5)-1, -1):
        b = a - j*j
        if b == 0:
            result=(min(result, 2))
            break
        for k in range(int(b**0.5), int((b//2)**0.5)-1, -1):
            c = b - k*k         
            if c == 0:
                result=(min(result, 3))
                break
print(result)
