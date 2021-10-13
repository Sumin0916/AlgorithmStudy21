import sys

def dfs(start):
    global res
    stack = [start]
    track = set()
    track.add(start)
    while stack:
        node = stack.pop()
        next_node = student[node]
        if not visited[next_node]:
            if next_node not in track:
                stack.append(next_node)
                track.add(next_node)
            else:
                if next_node == start:
                    return track
    return set()


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count = 0
    N = int(input())
    student = list(map(int, input().split()))
    student.insert(0, 0)
    visited = [False] * (N+1)
    res = set()
    for i in range(1, N+1):
        track = dfs(i)
        res = res | track
        for j in list(track):
            visited[j] = True
    print(N - len(res))