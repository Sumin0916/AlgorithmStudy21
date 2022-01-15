box = [True] * 10001
box[0] = False
box[1] = False
prime = []
N = int(input())

for i in range(2, 10001):
    if box[i]:
        prime.append(i)
        for j in range(2*i, 10001, i):
            box[j] = False

for i in range(1, 1229):
    if prime[i]*prime[i-1] > N:
        print(prime[i]*prime[i-1])
        break