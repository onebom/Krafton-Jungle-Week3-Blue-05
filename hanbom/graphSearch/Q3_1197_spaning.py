import sys
input=sys.stdin.readline

v,e=map(int, input().split())

# # -- 크루스칼 --
# def findRoot(x):
#     if x!=vroot[x]:
#         vroot[x]=findRoot(vroot[x])
#     return vroot[x]

# vroot=[i for i in range(v+1)]
# e_lst=[]
# for _ in range(e):
#     e_lst.append(list(map(int,input().split())))

# e_lst.sort(key=lambda x:x[2])

# rst=0
# for s, e, w in e_lst:
#     s_root=findRoot(s)
#     e_root=findRoot(e)
#     if s_root!=e_root:
#         if s_root>e_root: vroot[s_root]=e_root
#         else: vroot[e_root]=s_root
#         rst+=w

# print(rst)

#-- prim --
import heapq

visited=[False]*(v+1)
graph=[[] for _ in range(v+1)]
heap=[[0,1]]

for _ in range(e):
    a,b,c=map(int, input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

rst=0
cnt=0
while heap:
    print(heap)
    if cnt==v:
        break
    w,s=heapq.heappop(heap)
    print(w,s)
    if not visited[s]:
        visited[s]=True
        rst += w
        cnt+=1
        for i in graph[s]:
            heapq.heappush(heap,i)
    
print(rst)