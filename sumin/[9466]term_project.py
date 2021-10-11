T = int(input())


def find_parent(parent, x, count):
    if count > N:
        return x
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x], count+1)
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a, 0)
    b = find_parent(parent, b, 0)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(T):
    N = int(input())
    student = [x for x in range(N+1)]
    want_vote = list(map(int, input().split()))
    want_vote.insert(0, 0)
    res = set()
    ans = 0
    for i in range(1, N+1):
        a, b = i, want_vote[i]
        if find_parent(want_vote, a, 0) != find_parent(want_vote, b, 0):
            union_parent(want_vote, a, b)
    for i in range(1, N+1):
        if i not in res:
            res.add(i)
            ans += 1
    print(ans)
    print(want_vote)
            
        