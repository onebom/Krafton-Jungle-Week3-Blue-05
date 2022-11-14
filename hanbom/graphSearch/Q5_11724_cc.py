from itertools import cycle
import sys
input=sys.stdin.readline

def findRoot(x):
    if x!=vroot[x]:
        vroot[x]=findRoot(vroot[x])
    return vroot[x]

n,m=map(int,input().split())
vroot=[i for i in range(n+1)]

e_lst=[]
for _ in range(m):
    e_lst.append(list(map(int, input().split())))


for s,e in e_lst:
    s_root=findRoot(s)
    e_root=findRoot(e)
    if s_root!=e_root:
        if s_root>e_root:
            vroot[s_root]=e_root
        else: vroot[e_root]=s_root

cycle_root=[]
def checkCycle(i):    
    if i==vroot[i]:
        return i
    else:
        return checkCycle(vroot[i])
                    
for i in range(1,len(vroot)):
    root=checkCycle(i)
    cycle_root.append(root)

print(len(set(cycle_root)))