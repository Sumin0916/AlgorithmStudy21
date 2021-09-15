first = input()
second = input()
f_len = len(first)
s_len = len(second)

n = f_len if f_len > s_len else s_len
mem = [0] * (n+1)

