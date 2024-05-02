class TreeNode:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        self.root = self.insert_recursive(self.root, val)

    def insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)

        if root.val == key:
            return root
        elif root.val < key:
            root.right = self.insert_recursive(root.right, key)
        elif root.val > key:
            root.left = self.insert_recursive(root.left, key)
        return root        
    
    def indorder(self):
        self.inorder_recursive(self.root)
    
    def inorder_recursive(self, root):
        if root:
            self.inorder_recursive(root.left)
            print(root.val, end=' ')
            self.inorder_recursive(root.right)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(1)
    bst.insert(8)
    bst.insert(2)
    bst.insert(9)
    bst.insert(4)
    bst.indorder()