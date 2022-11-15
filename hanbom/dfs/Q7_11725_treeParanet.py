import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

def dfs(start,visited):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            rst[i]=start
            dfs(i,visited)

n=int(input())
graph=[[]for _ in range(n+1)]
rst=[[]for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(n-1):
    s,e=map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1,visited)
for i in rst[2:]:
    print(i)

        