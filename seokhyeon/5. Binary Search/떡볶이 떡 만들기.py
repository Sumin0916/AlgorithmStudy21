# 떡 개수, 요청한 떡의 길이
n, m = map(int, input().split())

# 떡 길이 리스트 입력받기
rc_array = list(map(int, input().split()))

rc_array.sort()

start = 0
end = rc_array[-1]

while start <= end:
    cut_length = 0
    mid = (start + end) // 2
    for length in rc_array:
        if length >= rc_array[mid]:
            cut_length += length - rc_array[mid]

    if m == cut_length:
        print(mid)
        break
    elif m > cut_length:
        end = mid - 1
    elif m < cut_length:
        start = mid + 1


