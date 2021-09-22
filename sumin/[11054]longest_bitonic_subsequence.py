N = int(input())
lst = list(map(int, input().split()))


def find_LIS(lst):
    mem = [0] * (N)
    for i in range(N):
        pre_mem = 0
        for j in range(i):
            if lst[i] > lst[j]:
                if pre_mem < mem[j]:
                    pre_mem = mem[j]
        mem[i] = pre_mem + 1
    return mem

f_res = find_LIS(lst)
s_res = find_LIS(lst[::-1])

max_res = 0

for i in range(1, N):
    max_res = max(max_res, max(f_res[:i])+max(s_res[:i]))

print(max_res)
