n = int(input())

dic = {}
score_board = []

for i in range(n):
    name, score = input().split()
    dic[int(score)] = name
    score_board.append(int(score))

score_board.sort()

for i in score_board:
    print(dic[i], end = ' ')


