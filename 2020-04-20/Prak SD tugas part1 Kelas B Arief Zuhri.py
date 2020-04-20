'''
Nama: Arief Zuhri
NIM: 19/447131/SV/16850
'''
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
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
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inOrderTraversal(self, root):
        res = []
        if root is not None:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
    
    def preOrderTraversal(self, root):
        res = []
        if root is not None:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res
    
    def postOrderTraversal(self, root):
        res = []
        if root is not None:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res
    
    def cekAngka(self, root, cari):
        if root is None:
            return False
        else:
            if root.data == cari:
                return True
            else:
                return (self.cekAngka(root.left, cari)) or (self.cekAngka(root.right, cari))
    
    def countNodes(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def countLeaves(self, root):
        if root.right is None and root.left is None:
            return 1
        else:
            return self.countLeaves(root.left) + self.countLeaves(root.right)
    
    def sumNodes(self, root):
        if root is None:
            return 0
        else:
            return root.data + self.sumNodes(root.left) + self.sumNodes(root.right)
    
    def heightTree(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.heightTree(root.left), self.heightTree(root.right))

    def bfs(self, root):
        visited = []
        if root:
            queue = []
            queue.append(root)
            
            while(len(queue)>0):
                visited.append(queue[0].data)
                cek = queue.pop(0)
                if cek.left:
                    queue.append(cek.left)
                if cek.right is not None:
                    queue.append(cek.right)
        return visited            

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root.printTree()
print(root.inOrderTraversal(root))
print(root.preOrderTraversal(root))
print(root.postOrderTraversal(root))
print(root.cekAngka(root, 31))
print(root.cekAngka(root, 30))
print(root.bfs(root))

print()
print("Hitung node =", root.countNodes(root))
print("Hitung leaf =", root.countLeaves(root))
print("Sum node =", root.sumNodes(root))
print("Tinggi tree =", root.heightTree(root))
