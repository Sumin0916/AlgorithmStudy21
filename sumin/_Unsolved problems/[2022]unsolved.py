import bisect

res_lst = []

def backtrack(string, lenth):
    if lenth < d:
        for i in range(d):
            if not visited[i]:
                string.append(str(i))
                visited[i] = True
                backtrack(string, lenth+1)
                visited[i] = False
                string.pop()
                
    elif lenth == d:
        res_lst.append(int("".join(string),d))
        return

N, d = map(int, input().split())
visited = [False] * d
backtrack([], 0)

if N >= res_lst[-1]:
    print(-1)
else:
    print(res_lst[bisect.bisect(res_lst, N)])
