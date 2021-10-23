N = int(input())
weight = [list(0 for _ in range(N+1))]
weight.extend(list([0] + list(map(int, input().split())) for _ in range(N)))
print(weight)