a, b = map(int, input().split())

def function(N):
    global remain
    if N == 0: return 0
    l = len(str(bin(N))) - 2  # 자릿수
    top = N-2**(l-1)+1
    botton = (l-1) * 2**(l-2)
    remain = function(N-2**(l-1))
    return int(top+botton+remain)

print(function(b)-function(a-1))
print(bin(15))

