import queue
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1] #서, 남, 동, 북

def bfs(x,y):
    queue=deque([[x,y]])
    visited[x][y]=True
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):    
            nx=x+dx[i]
            ny=y+dy[i]
            if nx >= 0 and nx<n and ny>=0 and ny<m:
                if (not visited[nx][ny]) and (graph[nx][ny]==1):
                    visited[nx][ny]=True
                    if graph[x][y]==1:
                                graph[nx][ny]=graph[x][y]+1
                    else:
                        graph[nx][ny]=min(graph[nx][ny],graph[x][y]+1)     
                    print(nx,ny)
                    print(graph)
                    queue.append([nx,ny])
        
                
                
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]

for idx in range(n):
    line_idx=list(map(int,list(input().strip())))
    graph[idx]=line_idx

bfs(0,0)
print(graph[n-1][m-1])
    