import sys

N, V = map(int, sys.stdin.readline().split())

parent = [0] * (N+1)

for i in range(1,N+1):
    parent[i] = i

def find_parent(parent:list,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for _ in range(V):
    a, b = map(int, sys.stdin.readline().split())
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    elif b < a :
        parent[a] = b

# 마지막 최신화
for i in range(1,N+1):
    if parent[i] != 0:
        find_parent(parent, i)

parent = parent[1:]

stack = []

for i in parent:
    if i not in stack:
        stack.append(i)

print(len(stack))