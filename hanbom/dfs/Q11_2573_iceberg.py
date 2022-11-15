import sys
import copy
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n,m=map(int, input().split())
ice_map= [[] for _ in range(n)]
for i in range(n):
    ice_map[i]=list(map(int, input().split()))

dx=[-1,0,1,0]
dy=[0,1,0,-1] # 북, 동, 남, 서

def dfs(x,y):
    visited[x][y]=0 # 내가 가본 곳= 0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if ice_map[nx][ny]==0 and visited[nx][ny]==1:
                if ice_map[x][y]>0:
                    ice_map[x][y]-=1
            else:
                if visited[nx][ny]==1:
                    dfs(nx,ny)

count=0
year=0
pre_map=[]
while True:
    visited=[[1]*m for _ in range(n)]
    num_bool=False
    for i in range(n):
        for j in range(m):
            if ice_map[i][j]!=0:
                num_bool=True
                dfs(i,j)
                if year==0:
                    pre_map=copy.deepcopy(ice_map)
                break
        if num_bool:
            break
    
    result=[visited[i][j]*pre_map[i][j] for j in range(m) for i in range(n)] 
    if year!=0:
        pre_map=copy.deepcopy(ice_map)
    year+=1
    if len(set(result))>2:
        print(year-1)
        break
    
    ice_val_lst= [ice_map[i][j] for j in range(m) for i in range(n)]
    if len(set(ice_val_lst))==1:
        print("0")
        break
