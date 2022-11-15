import sys
from itertools import permutations
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n=int(input())
a_lst=list(map(int,input().split()))
mt,mn,mp,dv=map(int,input().split())
c_lst=list("+"*mt+"-"*mn+"*"*mp+"/"*dv)

max_rst= -1e9
min_rst= 1e9

for case in permutations(c_lst):
    print(case)
    rst=a_lst[0]
    for idx in range(1,len(a_lst)):
        a1,a2=rst,a_lst[idx]
        cal=case[idx-1]
        if cal=="+": rst=a1+a2
        elif cal=="-": rst=a1-a2
        elif cal=="*": rst=a1*a2
        elif cal=="/": 
            if a1<0:
                rst=-((-a1)//a2)
            else:
                rst=a1//a2
    max_rst=max(max_rst,rst)
    min_rst=min(min_rst,rst)

def dfs(depth, total, plus, minus,multiply, divide):
    global max_rst, min_rst
    
    if depth == n:
        max_rst=max(total, max_rst)
        min_rst=min(total, min_rst)
        return
    
    if plus:
        dfs(depth+1, total+a_lst[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-a_lst[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*a_lst[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/a_lst[depth]), plus, minus, multiply, divide-1)

dfs(1, a_lst[0], mt, mn, mp, dv)
print(max_rst)
print(min_rst)


        