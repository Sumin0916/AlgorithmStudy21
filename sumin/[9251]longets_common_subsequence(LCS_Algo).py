first = input()
second = input()
f_len = len(first)
s_len = len(second)

if f_len >= s_len:
    first, second = second, first
    f_len, s_len = s_len, f_len

mem = [0] * (f_len)
for i in range(f_len):
    point = 0
    temp = 0
    for c1 in first[i:]:
        for c2i in range(point, s_len):
            print(c1, second[c2i])
            if c1 == second[c2i]:
                temp += 1
                point = c2i+1
                break
    print(first[i:])
    mem[i] = max(mem[i], temp)

# 우리는 문자열이 아니라 길이를 원하는 것이다.
print(mem)
