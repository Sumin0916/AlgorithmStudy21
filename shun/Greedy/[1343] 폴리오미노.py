sol = input()
sol = sol.replace('XXXX','AAAA')
sol = sol.replace('XX','BB')

if 'X' in sol:
    print(-1)
else:
    print(sol)