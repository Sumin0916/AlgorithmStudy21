#숫자카드게임

N,M = map(int,input().split())
card = []
card_min =[]

for i in range(N):
    card.append(list(map(int,input().split())))
    card_min.append(min(card[i]))

print(max(card_min))
