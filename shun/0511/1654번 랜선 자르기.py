K, N = list(map(int,input().split()))

for i in range(K):
    array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) //2
    for x in array:
        if x > mid:
            total += x-mid
    if x>mid:
        total += x -mid
    
    if total < N:
        end = mid -1
    else:
        result = mid
        start = mid +1

print(result)
