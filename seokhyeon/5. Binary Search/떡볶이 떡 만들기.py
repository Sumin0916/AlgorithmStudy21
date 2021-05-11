'''주어진 리스트에 너무 매몰될 필요는 없다.'''

# 떡 개수, 요청한 떡의 길이
n, m = map(int, input().split())

# 떡 길이 리스트 입력받기
rc_array = list(map(int, input().split()))

rc_array.sort()

start = 0
end = rc_array[-1]
result = 0

while start <= end:
    cut_length = 0
    mid = (start + end) // 2
    for length in rc_array:
        if length >= mid:
            cut_length += length - mid

    if m == cut_length:
        result = mid
        break
    elif m > cut_length:
        end = mid - 1
    elif m < cut_length:
        start = mid + 1
        result = max(mid, result) # 적어도 양 맞추기 = 최대한 떡 자르기

print(result)


