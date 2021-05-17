n, m = map(int, input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

cache = {}

def fcn(x, cache, coin_list):

    if x == 0:
        return 0

    if x < 0:
        return 10000

    cache[x] = 10001
    
    for coin in coin_list:
        cache[x] = min(cache[x], fcn(x - coin, cache, coin_list) + 1)
    
    return cache[x]

if fcn(m, cache, coin_list) == 10001:
    print(-1)
else:
    print(fcn(m, cache, coin_list))

print(coin_list)
print(cache)