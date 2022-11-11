import sys
input = sys.stdin.readline

class node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
class binary_search_tree():
    def __init__(self):
        self.root = None
    def insert(self, key):
        def _insert(pn, key):
            if key == pn.key:
                return False
            if key < pn.key:
                if not pn.left:
                    pn.left = node(key)
                else:
                    _insert(pn.left, key)
            else:
                if not pn.right:
                    pn.right = node(key)
                else:
                    _insert(pn.right, key)
            return True
        if not self.root:
            self.root = node(key)
            return True
        else:
            return _insert(self.root, key)
    def postorder(self):
        self.ret = []
        def _postorder(node):
            if not node:
                return
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            self.ret.append(node.key)
        _postorder(self.root)
        return self.ret

bst = binary_search_tree()
while True:
    try:
        i = int(input())
    except:
        break
    bst.insert(i)
print(*bst.postorder(), sep="\n")
