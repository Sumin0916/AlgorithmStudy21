formula = input()
mem = False
lenth = len(formula)

for i in range(0, lenth):
    char = formula[i]
    if formula[i] == "-":
        temp = list(formula)
        i += 1
        if mem:
            temp.insert(i-1, ")")
            mem = False
        else:
            temp.insert(i, "(")
            mem = True
        formula = "".join(temp)


if mem:
    temp = list(formula)
    temp.append(")")
    formula = "".join(temp)
    mem = False

lst = list(formula)
ind = 0
while True:
    lenth = len(lst)
    if ind > lenth-1:
        break
    

print(eval(formula))
