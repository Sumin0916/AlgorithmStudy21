import time

start = time.time()

# N, M, K 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first, second = data[n - 1], data[n - 2]

result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# 아래 코드와 비교

result = ((m // (k + 1)) * k + (m % (k + 1))) * first + (m // (k + 1)) * second


print(result)
finish = time.time()
print(finish - start)




