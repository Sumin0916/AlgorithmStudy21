# coin_list = [500, 100, 50, 10]
#
# change = int(input("money to give customer: "))
# cnt = 0
#
# for coin in coin_list:
#     if change//coin > 0:
#         cnt += change//coin
#         change = change%coin
#
# print(cnt)

def min_coin_cnt(change, coin_list):
    cnt = 0

    for coin in coin_list:
        if change//coin > 0:
            cnt += change // coin
            change = change % coin

    return cnt

coin_list1 = [500, 100, 50, 10]
x = int(input("change: "))
print(min_coin_cnt(x, coin_list1))