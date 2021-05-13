n, m = map(int, input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

cache = {}

def fcn(x, cache, coin_list):

    if x in coin_list:
        return 1
    
    if x < 0:
        return 0

    if x in cache:
        return cache[x]
    
    else:
        cache[x] = 10001
        for coin in coin_list:
                cache[x] = min(cache[x], fcn(x - coin, cache, coin_list) + 1)
    
    return cache[x]

print(fcn(m, cache, coin_list))
print(coin_list)
print(cache)