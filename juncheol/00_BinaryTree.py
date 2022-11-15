class Node :
    def __init__(self, key) :
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)

    def preorder(self): # 현재 방문중인 노드 = self
        if self != None :
            print(self.key)
            if self.left :
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self != None:
            if self.left :
                self.left.inorder()
            print(self.key)
            if self.right :
                self.right.inorder()
        
    def postorder(self):
        if self != None:
            if self.left :
                self.left.postorder()
            if self.right :
                self.right.postorder()
            print(self.key)



a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)

a.left = b
a.right = c
b.parent = a
c.parent = a
b.right = d
d.parent = b

