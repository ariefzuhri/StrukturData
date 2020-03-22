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

    def preOrderTraversal(self, root): # akar kiri kanan
        res = []
        if root is not None:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res

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

n = int(input())
a = list(map(int, input().split()))
deleteNode = int(input())

root = Node(a[0])
for i in range(1, n):
    root.insert(a[i])

root = root.delete(root, deleteNode)
print(" ".join(map(str, root.preOrderTraversal(root))))
