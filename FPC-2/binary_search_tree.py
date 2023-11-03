class Node:
    def __init__(self, data):
        self.data = data
        self.p = None
        self.left = None
        self.right = None


    def getData(self): return self.data
    def getParent(self): return self.p
    def getLeft(self): return self.left
    def getRight(self): return self.right   


    def isLeft(self):
        node_parent = self.getParent()
        if node_parent == None:
            return False
        if node_parent.getLeft() == self:
            return True
        return False


    def isRight(self):
        node_parent = self.getParent()
        if node_parent == None:
            return False
        if node_parent.getRight() == self:
            return True
        return False


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root


    def isEmpty(self):
        return self.root is None
    

    def tree_search(self, node, key): # O(h)
        if node == None or node.data == key:
            return node
        if key < node.data:
            return self.tree_search(node.left, key)
        else:
            return self.tree_search(node.right, key)
        

    def iterative_tree_search(self, node, key): # O(h)
        while node is not None and node.data != key:
            if key < node.data:
                node = node.left
            else:
                node = node.right
        return node
        

    def preorder_tree_walk(self, node): # θ(n)
        if node is not None:
            print(node.getData(), end=" ")
            self.preorder_tree_walk(node.left)
            self.preorder_tree_walk(node.right)


    def inorder_tree_walk(self, node): # θ(n)
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.getData(), end=" ")
            self.inorder_tree_walk(node.right)


    def postorder_tree_walk(self, node): # θ(n)
        if node is not None:
            self.postorder_tree_walk(node.left)
            self.postorder_tree_walk(node.right)
            print(node.getData(), end=" ")


    def tree_minimum(self, node): # O(h)
        while node.left is not None:
            node = node.left
        return node
    

    def tree_maximum(self, node): # O(h)
        while node.right is not None:
            node = node.right
        return node
    

    def tree_successor(self, node): # O(h)
        if node.right is not None:
            return self.tree_minimum(node.right)
        ancestor = node.p
        while ancestor != None and node == ancestor.right:
            node = ancestor
            ancestor = ancestor.p
        return ancestor
    

    def tree_predecessor(self, node): # O(h)
        if node.left is not None:
            return self.tree_maximum(node.left)
        ancestor = node.p
        while ancestor != None and node == ancestor.left:
            node = ancestor
            ancestor = ancestor.p
        return ancestor


    def tree_insert(self, node): # O(h)
        parent = None
        x = self.root
        while x is not None:
            parent = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.p = parent
        if parent == None: # a árvore estava vazia
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node


    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p


    def tree_delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y != z.right: # se o sucessor não for filho direito de z
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
        self.transplant(z, y)
        y.left = z.left
        y.left.p = y


if __name__ == "__main__":
    nodes_to_insert = [
        Node(41), Node(20), Node(11), Node(65), Node(50), 
        Node(45), Node(1), Node(55), Node(91), Node(99),
        Node(72), Node(29), Node(32), Node(15), Node(27)
    ]
    bst = BinarySearchTree()
    for node in nodes_to_insert:
        bst.tree_insert(node)
