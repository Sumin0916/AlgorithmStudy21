n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

# l = 0
for i in range(n):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
        l += 1
    else:
    #     pass

    # if l == k:
        break

print(sum(a))



    