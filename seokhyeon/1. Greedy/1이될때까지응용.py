import time
start = time.time()

# n, k 입력 받기
n, k = map(int, input().split())

# 횟수
cnt = 0

# 빼는 횟수는 한번에 처리하자!

while n >= k:
    cnt += n % k
    n -= n % k

    cnt += 1
    n //= k

cnt += (n - 1)

print(cnt)
end = time.time()
print(end - start)