import time
start = time.time()

# n, k 입력 받기
n, k = map(int, input().split())

# 횟수
cnt = 0

# n이 k로 나뉘기 전까진 -1

while n > 1:
    if n % k == 0:
        n = n /1/ k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)
end = time.time()
print(end - start)

