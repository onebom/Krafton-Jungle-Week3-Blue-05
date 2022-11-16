'''
import sys
from collections import deque

# 정점의 수
N = int(sys.stdin.readline().rstrip())

# 실내 : 1 , 실외 : 0
A = list(map(int, sys.stdin.readline().rstrip()))
A.insert(0, 0) # [0, 1, 0, 1, 1, 1]

graph = [[] for _ in range(N+1)]

for i in range(1,N):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(len(A)):
    if A[i] == 1:
        q = deque([i])
        visited = [None] * (N+1) # 새로운 출발지 선정마다 초기화
        while q :
            now = q.popleft()
            visited[now] = True
            for m in graph[now]:
                if not visited[m]:
                    visited[m] = True
                    if A[m] == 1: # 실내에 들리면 산책 끝
                        cnt += 1
                    elif A[m] == 0: # 실외면 다음 경로 탐색을 위해 append
                        q.append(m)

print(cnt)

76점 부분성공 코드
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def calPaths(graph: list, col: list) -> int:
    count = 0
    visited = set()

    def dfs(exterior: int) -> int:
        cnt = 0
        for neighbor in graph[exterior]:
            if col[neighbor] == 1:
                cnt += 1
            else:
                if neighbor not in visited:
                    visited.add(neighbor)
                    cnt += dfs(neighbor)
        return cnt

    for i in range(1, numVertices + 1):
        # 각 실내별 인접한 실내 구하기
        if col[i] == 1:
            for j in graph[i]:
                if col[j] == 1:
                    count += 1
        # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤 
        # 각 덩어리별로 n*(n-1)의 경우의 수를 계산
        else:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i)
                count += tmp * (tmp - 1)
 
    return count

if __name__ == '__main__':
    numVertices = int(input())
    col = list(map(int, list("0"+input().strip())))

    graph = [[] for _ in range(numVertices + 1)]
    
    for _ in range(1, numVertices):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(calPaths(graph, col))