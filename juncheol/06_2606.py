import sys

N = int(sys.stdin.readline().rstrip())
V = int(sys.stdin.readline().rstrip())

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

cnt = -1 # 1번 컴퓨터는 제외하고 카운트한다
for i in parent:
    if i == 1:
        cnt += 1

print(cnt)