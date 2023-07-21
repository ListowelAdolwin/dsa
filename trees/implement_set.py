class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Sett:
    root = None
    def __init__(self):
        pass

    def add(self, val, root=root):
        if not root:
            root = BST()
            return root
        if root.val < val:
            root.right = self.add(root.right, val)
        else:
            root.left = self.add(root.left, val)
        return root

    def remove(self, node, root=root):
        if not root:
            return
        if node > root.val:
            root.right = self.remove(node, root.right)
        elif node < root.val:
            root.left = self.remove(node, root.left)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                newnode = root.right
                while newnode and newnode.left:
                    newnode = newnode.left
                root.val = newnode.val
                root.right = self.remove(newnode.val, root.right)

        return root



    def inorder(self, root, result):
        if not root:
            return
        self.inorder(root.left, result)
        result.append(root.val)
        print(f"{root.val} -> ", end="")
        self.inorder(root.right, result)

# Create the binary tree
result = Sett()
result.add(7)
result.add(9)
print(result)

