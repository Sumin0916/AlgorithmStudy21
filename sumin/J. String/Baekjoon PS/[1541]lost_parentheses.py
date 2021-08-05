formula = list(input())
ind = 0
while True:
    if len(formula):
        if not int(formula[0]):
            formula.pop(0)
    else:
        break
if len(formula) == 0:
    formula.append(0)
while True:
    if ind == len(formula) - 1:
        break
    if formula[ind] == "+" or formula[ind] == '-':
        if formula[ind+1] == '0':
            formula.pop(ind+1)
            continue
    ind += 1
ind = 0
stat = False
while True:
    if ind > len(formula) - 1:
        break
    if formula[ind] == '-':
        formula.insert(ind+1, '(')
        ind += 1
        stat = True
    elif (formula[ind] == '+' or ind == len(formula) - 2) and stat:
        formula.insert(ind-1, ')')
        ind += 1
        stat = False
    ind += 1

print(formula)
