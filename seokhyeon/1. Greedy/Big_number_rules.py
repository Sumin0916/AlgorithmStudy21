import time

start = time.time()

N = int(input("size: "))
M = int(input("plus times: "))
K = int(input("constrain: "))

num_list = []

while len(num_list) < N:
    num = int(input("add number: "))
    num_list.append(num)

special_list = [0, num_list[0]]

for i in range(N):
    x = max(num_list[i], special_list[0])
    if x <= special_list[1]:
        special_list[0] = x
    else:
        special_list[0], special_list[1] = special_list[1], x

print(special_list)

find = 0
temp = K

if special_list[0] == special_list[1]:
    find = M * special_list[0]
    print(find)
else:
     for j in range(M):
        if K > 0:
             find += special_list[1]
             K -= 1
        else:
             find += special_list[0]
             K = temp
     print(find)

end = time.time()
print(end - start)




