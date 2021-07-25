import sys

n = int(sys.stdin.readline().rstrip())
seq = []

for _ in range(n):
    seq.append(int(input()))

num_ary = [x for x in range(1, n+1)]
res_ary = [0]
answer = []

for num in seq:
    if num in num_ary:
        dif = num - res_ary[-1]
        for _ in range(dif):
            answer.append("+")
            res_ary.append(num_ary.pop(0))
        answer.append("-")
        res_ary.pop()

    else:
        if res_ary[-1] == num:
            answer.append("-")
            res_ary.pop()
        else:
            answer.append(-1)
            break
print(num_ary)
print(res_ary)
print(answer)
if answer[-1] == -1:
    print("NO")
else:
    for c in answer:
        print(c)



