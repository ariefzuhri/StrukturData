class Node:
    def __init__(self, data):
        self.left = None;
        self.right = None;
        self.data = data # Insert node
        
    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            # Jika root belum ada data:
            self.data = data
    
    # Print the tree
    def printTreeInOrder(self):
        if self.left:
            self.left.printTreeInOrder()
        print(self.data)
        if self.right:
            self.right.printTreeInOrder()
    
    def printTreePreOrder(self):
        print(self.data)
        if self.left:
            self.left.printTreePreOrder()
        if self.right:
            self.right.printTreePreOrder()
    
    def printTreePostOrder(self):
        if self.left:
            self.left.printTreePostOrder()
        if self.right:
            self.right.printTreePostOrder()
        print(self.data)

    # Traversal
    def inOrderTraversal(self, root): # kiri akar kanan
        res = []
        if root is not None:
            res = self.inOrderTraversal(root.left) # Isi res dengan node-node di kiri
            res.append(root.data) # Append res dengan node root
            res = res + self.inOrderTraversal(root.right) # Tambah isi res dengan node-node di kanan
        return res
    
    def preOrderTraversal(self, root): # akar kiri kanan
        res = []
        if root is not None:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res
    
    def postOrderTraversal(self, root): # kiri kanan akar
        res = []
        if root is not None:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res

    # Tugas nomor 5-10:
    def findMax(self, root):
        # Nilai max selalu terletak di kanan
        if root.right is None:
            return root.data
        return self.findMax(root.right)
    
    def findMin(self, root):
        # Nilai min selalu terletak di kiri
        if root.left is None:
            return root.data
        return self.findMin(root.left)
    
    def cari(self, root, x):
        # Jika penelusuran sudah lebih dari node terakhir
        if root is None:
            return False
        
        # Cek
        if x == root.data:
            return True
        # Penelusuran
        elif x > root.data: # Jika lebih dari, telusuri ke kanan
            return self.cari(root.right, x)
        elif x < root.data: # Jika kurang dari, telusuri ke kiri
            return self.cari(root.left, x)
    
    def count(self, root):
        if root is None:
            return 0
        else:
            # Hitung root + semua node di kiri + semua node di kanan
            return 1 + self.count(root.left) + self.count(root.right)
        
    def deleteTree(self, root, subTree): 
        if root is None:
            return None
        
        if subTree.data > root.data:
            root.right = self.deleteTree(root.right, subTree)
        elif subTree.data < root.data:
            root.left = self.deleteTree(root.left, subTree)
        elif subTree.data == root.data:
            root = None
        
        return root

    def delete(self, root, data):
        if root is None:
            return None

        # If current node's data is less than that of root node, then only search in left subtree else right subtree
        if data > root.data:
            root.right = self.delete(root.right, data)
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data == root.data:
            # Deleting node with one child/no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Deleting node with two children
            elif root.right is not None and root.left is not None:
                # First get the inorder successor
                # Mencari pengganti node
                temp = root.minValueNode(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, temp.data)

        return root
    
    def minValueNode(self, node):
        current = node
        # Loop down to find the leftmost leaf
        # Node pengganti terletak di subtree kanan dan paling kiri
        while(current.left is not None):
            current = current.left
        return current

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.inOrderTraversal(root))
root.printTreeInOrder()
print()

print(root.preOrderTraversal(root))
root.printTreePreOrder()
print()

print(root.postOrderTraversal(root))
root.printTreePostOrder()
print()

print("Nilai tertinggi =", root.findMax(root))
print("Nilai terendah =", root.findMin(root))
print()

print("Apakah 10 ada?", root.cari(root, 10))
print("Apakah 19 ada?", root.cari(root, 19))
print("Apakah 27 ada?", root.cari(root, 27))
print("Apakah 42 ada?", root.cari(root, 42))
print("Apakah 100 ada?", root.cari(root, 100))

print("Banyaknya node =", root.count(root))
print()

print("Sebelum  in:", root.inOrderTraversal(root))
print("Sebelum pre:", root.preOrderTraversal(root))
print("Sebelum pos:", root.postOrderTraversal(root))

root = root.delete(root, 42)
root = root.deleteTree(root, root.right)
root = root.delete(root, 27)
print()

print("Sesudah  in:", root.inOrderTraversal(root))
print("Sesudah pre:", root.preOrderTraversal(root))
print("Sesudah pos:", root.postOrderTraversal(root))
