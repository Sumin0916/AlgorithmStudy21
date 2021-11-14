def turn_stat(order):
    global stat
    p_lst = [order, order+10, order-10, order+1, order-1]
    for o in p_lst:
        if 0 <= o < 100:
            stat ^= (1<<o)


