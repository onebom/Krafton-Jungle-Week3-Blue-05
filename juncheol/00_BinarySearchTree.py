class BST :
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__() # generator , class Node preorder

    def finde_loc(self, key) : # key값 노드가 있다면 해당 노드 return / 없다면 노드가 삽입될 부모 노드 리턴
        if self.size == 0:
            return None

        p = None
        v = self.root

        while v != None:
            if v.key == key : return v
            elif v.key < key :
                p = v
                v = v.right
            else :
                p = v
                v = v.left
        
        return p

    def search(self, key) :
        r = self.finde_loc(key)
        if v == None :
            return None
        else:
            return v

    def insert(self, key):
        p = self.finde_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= key :
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            print("key is already in tree")
            return p # p = None