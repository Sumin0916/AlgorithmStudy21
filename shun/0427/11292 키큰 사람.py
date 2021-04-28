while True:
    N = int(input())
    if N>0:
        a = []
        for i in range(N):
            name, length = input().split()
            length = float(length)
            a.append([name, length])
        a.sort(key= lambda x: x[1], reverse=True)
        for e in a:
            if a[0][1] == e[1]:
                print(e[0],end=" ")
    else:
        break
    

    

