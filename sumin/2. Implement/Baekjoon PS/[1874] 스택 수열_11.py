"""
스택 수열
"""
n = int(input())
nums_list = []
continus_num = [i for i in range(n, 0, -1)]
stack = [0, 0]
history_move = []
res = 0

for i in range(n):
    nums_list.append(int(input()))

for num in nums_list:
    while True:
        if stack[-1] != num and stack[-2] != num: # 이부분 수정이 필요함
            res += 1
            break
        
        if stack[-1] == num:
            stack.pop()
            history_move.append("-")
            break
        
        else:
            stack.append(continus_num.pop())
            history_move.append("+")

if res != 0:
    print("NO")

else:
    for his in history_move:
        print(his)