string = input()
string_len = len(string)
mem = [[0] * (string_len+1) for _ in range(string_len+1)]
result = [float('inf')] * (string_len+1)
result[0] = 0

for i in range(1, string_len+1):
    mem[i][i] = 1

for i in range(1, string_len):
    if string[i] == string[i-1]:
        mem[i][i+1] = 1

for i in range(2, string_len+1):
    for j in range(1, string_len+1-i):
        if string[j-1] == string[j+i-1] and mem[j+1][j+i-1] == 1:
            mem[j][j+i] = 1

for i in range(1, string_len+1):
    result[i] = min(result[i], result[i-1] + 1)
    for j in range(i+1, string_len+1):
        if mem[i][j] != 0:
            result[j] = min(result[j], result[i-1] + 1)

print(result[string_len])
