start = input()

row = ['1', '2', '3', '4', '5', '6', '7', '8']
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

trans_row = [2, 2, -2, -2, 1, 1, -1, -1]
trans_col = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0

row_index = 0
col_index = 0

for i in range(8):
    if row[i] in start:
        row_index = i
    if col[i] in start:
        col_index = i

for k in range(8):
    if row_index + trans_row[k] >= 0 and row_index + trans_row[k] <= 7 and col_index + trans_col[k] >= 0 and col_index + trans_col[k] <= 7:
        result += 1

print(result)

    
    



