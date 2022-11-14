import sys
from collections import deque

input=sys.stdin.readline

def bfs(graph, start, visited):
    global cnt
    
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                cnt+=1
                

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
cnt=0

for _ in range(m):
    s,e= map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

print(graph)
bfs(graph,1,visited)
print(cnt)