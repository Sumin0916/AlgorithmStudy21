N = int(input())

res = input()
string_len = len(res[0])

for _ in range(N-1):
    new_string = input()
    new_res = ""
    print(res, new_string)
    for i in range(string_len):
        if res[i] == new_string[i]:
            new_res += new_string[i]
        res = new_res
print(res)