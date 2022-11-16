import sys


# 수열의 개수
N = int(sys.stdin.readline().rstrip())

# 수열
A = list(map(int, sys.stdin.readline().split()))

# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
a, b, c, d = list(map(int, sys.stdin.readline().split()))


maxValue = -sys.maxsize
minValue = sys.maxsize

def dfs(n, value, plus, minus, multiply, divide):
    global minValue
    global maxValue
    if n == N :
        maxValue = max(maxValue, value)
        minValue = min(minValue, value)
        return
    if plus:
        dfs(n+1, value + A[n], plus - 1, minus, multiply, divide)
    if minus:
        dfs(n+1, value - A[n], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(n+1, value * A[n], plus, minus, multiply - 1, divide)
    if divide:
        dfs(n+1, int(value / A[n]), plus, minus, multiply, divide - 1)
dfs(1,A[0],a,b,c,d)
print(maxValue)
print(minValue)