n = int(input())
fear_list = list(map(int, input().split()))

# 공포도 낮은 순대로
fear_list.sort(reverse= True)
max_group = 0

for i in range(len(fear_list)):
    group = 0
    end_point = 0
    while True:
        # 그룹에 마지막 index 자리
        end_point = i + fear_list[i] - 1
        if end_point < len(fear_list) - 1:
            i = end_point + 1
            group += 1
        # end_point가 list의 마지막 index일 때 
        elif end_point == len(fear_list) - 1:
            group += 1
            max_group = max(max_group, group)
            break
        # end_point가 list의 마지막 index 넘어갈 때
        elif end_point > len(fear_list) - 1:
            max_group = max(max_group, group)
            break

print(max_group)




