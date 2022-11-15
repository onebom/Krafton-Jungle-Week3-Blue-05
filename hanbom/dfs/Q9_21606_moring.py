import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

def dfs(start,visited):
    global cnt
    visited[start]=True
    for v in graph[start]:
        if not visited[v]:
            if a[v-1]==1:
                visited[v]=True
                cnt+=1
            else:
                dfs(v,visited)

n=int(input())
a=list(map(int,list(input().strip())))
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
    
cnt=0
for i in range(1, n+1):
    if a[i-1]==1:
        dfs(i,[False]*(n+1))

print(cnt)