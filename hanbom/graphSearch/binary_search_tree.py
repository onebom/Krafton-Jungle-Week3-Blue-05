import sys
input=sys.stdin.readline

class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def add(self, key):
        def _add(node, key)->None:
            if key==node.key:
                exit()
            elif key<node.key:
                if node.left is None:
                    node.left=Node(key)
                else:
                    _add(node.left, key)
            else:
                if node.right is None:
                    node.right=Node(key)
                else:
                    _add(node.right,key)
                    
        if self.root is None:
            self.root=Node(key)
        else:
            _add(self.root,key)
            
    def dumb(self):
        def print_subtree(node):
            if node is not None:     
                print_subtree(node.left)
                print_subtree(node.right)
                print(f'{node.key}')
        print_subtree(self.root)

tree=BinaryTree()
while True:
    try:
        item=int(input())
    except:
        break
    tree.add(item)

tree.dumb()