x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

gradiant1 = (y2-y1)/(x2-x1)
right1 = (gradiant1 * x3) + y2 - (gradiant1*x2)
right2 = (gradiant1 * x4) + y2 - (gradiant1*x2)

if y3 == right1 or y4 == right2:
    print(1)
elif y3 > right1 and y4 < right2:
    print(2)
elif y3 < right1 and y4 > right2:
    print(3)
else:
    print(0)



