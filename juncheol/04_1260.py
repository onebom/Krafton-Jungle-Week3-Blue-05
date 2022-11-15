import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

visited = [False] * (N+1)
graph = [[]] * (N+1)

for _ in range(1,M+1): # 그래프 그리기
    node, v = map(int, sys.stdin.readline().split())
    edges = graph[node][:]
    edges.append(v)
    edges.sort()
    graph[node] = edges

    edges = graph[v][:]
    edges.append(node)
    edges.sort()
    graph[v] = edges

def dfs(graph:list, v:int, visited:list):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph,V,visited)
print()
# BFS 초기화
visited = [False] * (N+1)

def bfs(graph:list, v:int, visited:list):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(graph, V, visited)