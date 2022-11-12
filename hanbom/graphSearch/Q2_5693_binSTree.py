import sys
sys.setrecursionlimit(10**5)

tree=[]
while True:
    try: tree.append(int(sys.stdin.readline()))
    except: break

def postorder(l,r):
    if l>r:
        return 
    mid=r+1
    
    for i in range(l+1,r+1): # 루트 밑을 다 보겠다
        if tree[l]<tree[i]: # 오른쪽이라면
            mid=i
            break
    
    postorder(l+1,mid-1) # 왼쪽 보기
    postorder(mid, r) # 오른쪽 보기
    print(tree[l]) # 나(루트) 출력

postorder(0,len(tree)-1)
         
    