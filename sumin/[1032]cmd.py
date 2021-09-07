N = int(input())

res = 0
last = ""
for _ in range(N):
    string = input()
    for i in range(len(last)):
        if last[i] == string[i]:
            res = i
    last = string

print(string[:res+1])
