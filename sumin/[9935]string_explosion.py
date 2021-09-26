string = list(input())
explosion_string = list(input())
len_string = len(string)
len_ex = len(explosion_string)
ind = 0

while True:
    ind = max(ind, 0)
    if ind >= len_string:
        break
    if string[ind] == explosion_string[0]:
        stat = True
        for i in range(1, len_ex):
            tind = ind + i
            if tind < len_string:
                if string[tind] != explosion_string[i]:
                    stat = False
                    break
            else:
                stat = False
        if stat:
            del string[ind:ind+len_ex]
            len_string -= len_ex
            ind -= len_ex
        else:
            ind += 1
    else:
        ind += 1
if string:
    print("".join(string))
else:
    print("FRULA")
