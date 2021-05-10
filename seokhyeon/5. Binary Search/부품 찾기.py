n = int(input())
list1 = list(map(int, input().split()))
list1.sort()
m = int(input())
list2 = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

for i in range(m):
    k = binary_search(list1, list2[i], 0, n - 1)
    if k != None:
        print('yes', end = ' ')
    else:
        print('No', end = ' ') 