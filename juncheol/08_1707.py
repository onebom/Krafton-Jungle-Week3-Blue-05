import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())
res = []
for _ in range(K):

    V, E = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    direction = [[] for _ in range(V+1)]
    q = deque([1])
    direction[1] = 'left'
    result = ''
    while q:
        now = q.popleft()
        arrow = direction[now]
        for i in graph[now]:
            if not direction[i]:
                if arrow == 'left':
                    direction[i] = 'right'
                else:
                    direction[i] = 'left'
                q.append(i)
            elif direction[i] == arrow:
                result = "NO"
                q = deque([])
                break
        if not q:
            try:
                a = direction[1:].index([])
                q.append(a+1)
                direction[a+1] = 'left'
            except:
                pass
    if not result:
        result = "YES"
    
    res.append(result)

for i in res:
    print(i)