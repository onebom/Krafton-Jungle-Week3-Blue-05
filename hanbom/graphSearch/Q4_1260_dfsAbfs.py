import queue
import sys
from collections import deque

input=sys.stdin.readline

n,m,v=map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
    
    graph[s].sort()
    graph[e].sort()

print(graph)

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(graph, start,visited):
    visited[start]=True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph,v,[False]*(n+1))
print()
bfs(graph,v,[False]*(n+1))