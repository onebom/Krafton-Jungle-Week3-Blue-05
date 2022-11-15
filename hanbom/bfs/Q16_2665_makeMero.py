import sys
input=sys.stdin.readline

m,n,h=map(int,input().split())
graph=[[False]*(n) for _ in range(h)]
# print(graph)
for h_idx in range(h):
    for n_idx in range(n):
        graph[h_idx][n_idx]=list(map(int,input().split()))
        
print(graph[0][0])
    