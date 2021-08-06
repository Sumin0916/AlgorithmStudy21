N = int(input())
string_len = int(input())
string = input()

P_N = "I" + ("OI" * N)

ind = 0
res = 0

while True:
    if ind >= string_len:
        break
    if string[ind:ind+2*N+1] == P_N:
        ind += 2*N
        res += 1
    else:
        ind += 1

print(res)