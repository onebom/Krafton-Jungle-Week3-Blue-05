import queue
import sys
from collections import deque
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10)
input=sys.stdin.readline
INF=10000000

def bfs(start):
    queue=deque([start])
    distance[start]=0
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if distance[i]==INF:
                distance[i]=min(distance[i], distance[v]+1)
                queue.append(i)
            
                
n,m,k,x=map(int,input().split())
graph=[[]for _ in range(n+1)]
distance=[ INF for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    graph[s].append(e)

bfs(x)
rest_list = list(filter(lambda x: distance[x] == k, range(len(distance))))
if rest_list:
    for r in rest_list:
        print(r)
else:
    print("-1")          