N, M = map(int, input().split())
temp = list(map(int, input().split()))
temp = temp[1:]
known = set(temp)
res = 0
party_lst = []

for _ in range(M):
    temp = list(map(int, input().split()))
    temp = temp[1:]
    party_lst.append(set(temp))


def back(ind, count):
    global res, known
    if ind == M:
        print(known, res)
        res = max(res, count)
        return
    inter = party_lst[ind] & known

    if inter == set():  # 파티에 진실을 아는 사람이 없을 때
        back(ind+1, count+1)  # 거짓말
        known.union(inter)
        back(ind+1, count)  # 진실
        known.difference(inter)
    else:  # 진실을 아는 사람이 있을 때(무조건 진실을 이야기 한다.)
        known.union(inter)
        back(ind+1, count)
        known.difference(inter)


back(0, 0)
print(res)
