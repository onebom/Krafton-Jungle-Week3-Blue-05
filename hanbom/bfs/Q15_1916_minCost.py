import sys
input=sys.stdin.readline
INF=100000000

n=int(input())
m=int(input())
graph=[[]for _ in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])

start,end=map(int,input().split())
# print(graph)

def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if not visited[i] and distance[i]<min_value:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    distance[start]=0
    visited[start]=True
    
    for i in graph[start]:
        distance[i[0]]=min(distance[i[0]],i[1])
    
    for _ in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        for next in graph[now]:
            cost=distance[now]+next[1]
            if cost<distance[next[0]]:
                distance[next[0]]=cost
        
dijkstra(start)
# print(distance)
print(distance[end])

