import sys

N = int(sys.stdin.readline().rstrip())
nodeList = []
for i in range(N):
    node = list(map(str, sys.stdin.readline().rstrip().split(' ')))
    nodeList.append(node)


preStack = ''
def preorder(node:str):
    global preStack
    for i in nodeList:
        if i[0] == node:
            preStack = preStack + node
            if i[1] != '.':
                preorder(i[1])
            if i[2] != '.':
                preorder(i[2])
            return

preorder(nodeList[0][0])


inStack = ''
def inorder(node:str):
    global inStack
    for i in nodeList:
        if i[0] == node:
            if i[1] != '.':
                inorder(i[1])
            inStack = inStack + node
            if i[2] != '.':
                inorder(i[2])
            return

inorder(nodeList[0][0])


postStack = ''
def postorder(node:str):
    global postStack
    for i in nodeList:
        if i[0] == node:
            if i[1] != '.':
                postorder(i[1])
            if i[2] != '.':
                postorder(i[2])
            postStack = postStack + node
            return

postorder(nodeList[0][0])



print(preStack)
print(inStack)
print(postStack)