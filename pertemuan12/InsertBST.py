class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def Insert(self,data):
        new = Node(data)
        if self.root == None:
            self.root = new
            return
        
        P = self.root
        Q = self.root
        while Q != None and new.data != P.data:
            P = Q
    
            if new.data < Q.data:
                Q = P.left 
            else:
                Q = P.right

        if new.data == P.data:
            print("data sudah ada")
            return
        
        if new.data < P.data:
            P.left = new
        else:
            P.right = new

    
def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)
    


bst = BinarySearchTree()
bst.Insert(10)
bst.Insert(5)
bst.Insert(15)
bst.Insert(12145)
bst.Insert(55523)
bst.Insert(15635)

in_order(bst.root)