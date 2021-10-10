N = int(input())
box = [True] * (N+1)
box[:2] = [False, False]
std = int(N**(0.5))+1

for i in range(2, std):
    if box[i]:
        for j in range(2*i, N+1, i):
            box[j] = False

prime_num = [x for x in range(2, N+1) if box[x]]
print(prime_num)