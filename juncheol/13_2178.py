import sys
sys.setrecursionlimit(10**5)

N, M = map(int, sys.stdin.readline().split())

nodes = []

for i in range(N):
    nodes.append(list(map(int, sys.stdin.readline().rstrip())))

# 상 하 좌 우
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]
stack = []
cnt = 0
def bfs(x,y,cnt):
    # 해당 노드가 1이며, x 와 y 좌표가 범위 안에 있어야 한다.
    if  N > x >= 0 and M > y >= 0:
        if x == N-1 and y == M-1: # 골인지점 도달 시
            nodes[x][y] = cnt
            cnt += 1
            stack.append(cnt)
            return
        elif nodes[x][y] == 1 or cnt < nodes[x][y]:
            nodes[x][y] = cnt
            cnt += 1
            for i in range(4):
                bfs(x+mx[i], y+my[i], cnt)
    return
bfs(0,0,cnt)

stack.sort()
print(stack[0])