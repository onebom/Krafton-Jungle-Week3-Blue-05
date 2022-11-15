import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
visited = [False] * (N+1)


for i in range(1,N+1):
    parent[i] = i


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for _ in range(N-1):
    a , b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()
    

q = deque([1])
while q :
    now = q.popleft()
    for i in graph[now]:
        if not visited[i]:
            parent[i] = now
            visited[i] = True
            q.append(i)

parent = parent[2:]
for i in parent:
    print(i)