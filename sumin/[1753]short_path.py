import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [list(False for _ in range(V+1)) for _ in range(V+1)]
for _ in range(E):
    
