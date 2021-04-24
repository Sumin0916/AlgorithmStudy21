adv_nums = int(input())
adv_fears = list(map(int, input().split()))

adv_fears.sort()
counter = 0

while adv_fears:
    del adv_fears[-(adv_fears[-1]):]
    counter += 1

print(counter)