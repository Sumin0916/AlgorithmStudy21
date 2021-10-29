import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
direc_lst = ["up", "down", "left", "right"]
ans = 0


def rotating(direc, graph):
    global N
    new_graph = [list(0 for _ in range(N)) for _ in range(N)]
    if direc == "left":
        for i in range(N):
            for j in range(N):
                new_graph[N-j-1][i] = graph[i][j]
    elif direc == "right":
        for i in range(N):
            for j in range(N):
                new_graph[j][N-i-1] = graph[i][j]
    return new_graph


def moving_line(graph):
    global N
    for i in range(N):
        visited = set()
        for j in range(N-1, -1, -1):
            now_num = graph[j][i]
            graph[j][i] = 0
            if now_num == 0:
                continue
            for k in range(1, N):
                if j + k >= N:
                    graph[j+k-1][i] = now_num
                    break
                if graph[j+k][i] == now_num:
                    if j+k not in visited:
                        visited.add(j+k)
                        graph[j+k][i] = 2 * now_num
                        break
                    else:
                        graph[j+k-1][i] = now_num
                        break
                elif graph[j+k][i] != 0 and graph[j+k][i] != now_num:
                    graph[j+k-1][i] = now_num
                    break

def slide_map(direc, graph):
    if direc == "up":
        graph = rotating("left", graph)
        graph = rotating("left", graph)
        moving_line(graph)
        graph = rotating("left", graph)
        graph = rotating("left", graph)

    elif direc == "down":
        moving_line(graph)

    elif direc == "left":
        graph = rotating("left", graph)
        moving_line(graph)
        graph = rotating("right", graph)


    elif direc == "right":
        graph = rotating("left", graph)
        moving_line(graph)
        graph = rotating("right", graph)
    return graph

def cal(graph, cnt):
    global direc_lst, ans
    if cnt == 6:
        #for i in graph:
            #print(*i)
        #print()
        ans = max(ans, max(list(map(max, graph))))
        return
    for i in range(4):
        cal(slide_map(direc_lst[i], graph), cnt+1)
    


print(ans)

