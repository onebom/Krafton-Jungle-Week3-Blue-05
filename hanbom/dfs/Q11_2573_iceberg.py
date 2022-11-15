import sys
input=sys.stdin.readline

n,m=map(int, input().split())
ice_map= [[] for _ in range(n)]
for i in range(n):
    ice_map[i]=list(map(int, input().split()))
visited=[[False]*m for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,-1,0,1] # 서, 북, 동, 남

print(ice_map[1])
# def dfs(x,y):
#     visited[x][y]=True
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
        
#         if nx>=0 and nx<=n and 