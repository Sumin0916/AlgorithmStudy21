'''set 활용'''
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set)자료형에 기록
array = set(map(int, input().split()))

m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공배긍로 구분하여 입력
x = list(map(int, input().split()))

# 손임이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

