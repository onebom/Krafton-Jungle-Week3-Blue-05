import sys
from collections import deque

# N : 도시의 개수, M : 도로의 개수, K : 거리 정보, X : 출발도시 번호
N, M, K, X = map(int, sys.stdin.readline().split())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M): # 그래프 그리기
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

dis = [0 for _ in range(N+1)] # 거리

q = deque([X]) # bfs 탐색을 위한 queue 세팅
visited[X] = True # 시작 도시 방문
while q:
    now = q.popleft()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            dis[i] = dis[now] + 1 # 해당 거리는 부모의 거리 + 1
            q.append(i)

res = []
for i in range(1,N+1):
    if dis[i] == K :
        res.append(i)

if res :
    for i in res:
        print(i)
else:
    print(-1)