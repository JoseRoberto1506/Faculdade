class Node:
    def __init__(self, data, color="BLACK", p=None, left=None, right=None):
        self.data = data
        self.color = color
        self.p = p
        self.left = left
        self.right = right


    def getData(self): return self.data
    def getColor(self): return self.color
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


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.p = self.nil
        self.left = self.nil
        self.right = self.nil
        self.root = self.nil

    
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
    

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)
    

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.right) - self.height(node.left)
    

    def left_rotate(self, node): # O(1)
        y = node.right
        node.right = y.left     # torna a sub-árvore esquerda de y na sub-árvore direita do nó a ser rotacionado
        if y.left is not None:
            y.left.p = node
        y.p = node.p            # conecta o pai do nó a ser rotacionado a y
        if node.p is None:
            self.root = y
        elif node.isLeft():
            node.p.left = y
        else:
            node.p.right = y
        y.left = node           # coloca o nó rotacionado na esquerda de y
        node.p = y


    def right_rotate(self, node): # O(1)
        x = node.left
        node.left = x.right     # torna a sub-árvore direita de x na sub-árvore esquerda do nó a ser rotacionado
        if x.right is not None:
            x.right.p = node
        x.p = node.p            # conecta o pai do nó a ser rotacionado a x
        if node.p is None:
            self.root = x
        elif node.isLeft():
            node.p.left = x
        else:
            node.p.right = x
        x.right = node          # coloca o nó rotacionado na direita de x
        node.p = x

    
    def rb_insert(self, z): # O(lg n)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "RED"
        self.rb_insert_fixup(z)


    def rb_insert_fixup(self, z):
        while z.p.color == "RED":
            if z.p.isLeft():
                # Caso 1: o tio y de z é vermelho
                y = z.p.p.right
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                # Caso 2: o tio de z é preto e z é um filho à direita
                elif z.isRight():
                    z = z.p
                    self.left_rotate(z)
                # Caso 3: o tio y de z é preto e z é um filho à esquerda
                z.p.color = "BLACK"
                z.p.p.color = "RED"
                self.right_rotate(z.p.p)
            elif z.p.isRight():
                # Caso 1: o tio y de z é vermelho
                y = z.p.p.left
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                # Caso 2: o tio de z é preto e z é um filho à esquerda
                elif z.isLeft():
                    z = z.p
                    self.right_rotate(z)
                # Caso 3: o tio y de z é preto e z é um filho à direita
                z.p.color = "BLACK"
                z.p.p.color = "RED"
                self.left_rotate(z.p.p)
        self.root.color = "BLACK"


    def rb_transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u.isLeft():
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p


    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == "BLACK":
            self.rb_delete_fixup(x)


    def rb_delete_fixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x.isLeft():
                w = x.p.right
                if w.color == "RED":
                    # Caso 1: o irmão w de x é vermelho
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    # Caso 2: o irmão w de x é preto e os filhos de w são pretos
                    w.cor = "RED"
                    x = x.p
                elif w.right.color == "BLACK":
                    # Caso 3: o irmão w de x é preto, o filho à esquerda de w é vermelho e o filho à direita de w é preto
                    w.left.color = "BLACK"
                    w.color = "RED"
                    self.right_rotate(w)
                    w = x.p.right
                    # Caso 4: o irmão w de x é preto e o filho à direita de w é vermelho
                    w.color = x.p.color
                    x.p.color = "BLACK"
                # Caso 4: o irmão w de x é preto e o filho à direita de w é vermelho
                w.right.color = "BLACK"
                self.left_rotate(x.p)
                x = self.root
            else:
                w = x.p.left
                if w.color == "RED":
                    # Caso 1: o irmão w de x é vermelho
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    # Caso 2: o irmão w de x é preto e os filhos de w são pretos
                    w.cor = "RED"
                    x = x.p
                elif w.left.color == "BLACK":
                    # Caso 3: o irmão w de x é preto, o filho à esquerda de w é vermelho e o filho à direita de w é preto
                    w.right.color = "BLACK"
                    w.color = "RED"
                    self.left_rotate(w)
                    w = x.p.left
                    # Caso 4: o irmão w de x é preto e o filho à direita de w é vermelho
                    w.color = x.p.color
                    x.p.color = "BLACK"
                # Caso 4: o irmão w de x é preto e o filho à direita de w é vermelho
                w.left.color = "BLACK"
                self.right_rotate(x.p)
                x = self.root
        x.color = "BLACK"


if __name__ == "__main__":
    values_to_insert = [
        41, 20, 11, 65, 50, 
        45, 1, 55, 91, 99,
        72, 29, 32, 15, 27
    ]
    rb_tree = RedBlackTree()
    for value in values_to_insert:
        rb_tree.rb_insert(Node(value))
