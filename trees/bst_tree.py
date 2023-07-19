class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def insert(self, root, val):
        if not root:
            return BST(val)
        if root.val < val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        return root

    def delete_node(self, root, node):
        if not root:
            return
        if node.val > root.val:
            root.right = self.delete_node(root.right, node)
        elif node.val < root.val:
            root.left = self.delete_node(root.left, node)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                newnode = root.right
                while newnode and newnode.left:
                    newnode = newnode.left
                print(f"{root.val} successfully deleted from bst")
                root.val = newnode.val
                root.right = self.delete_node(root.right, newnode)

        return root



    def inorder(self, root, result):
        if not root:
            return
        self.inorder(root.left, result)
        result.append(root.val)
        print(f"{root.val} -> ", end="")
        self.inorder(root.right, result)

# Create the binary tree
tree = BST(4)
tree.left = BST(2)
tree.right = BST(6)
tree.left.left = BST(1)
tree.left.right = BST(3)
tree.right.left = BST(5)
tree.right.right = BST(7)

sol = Solution()
sol.inorder(tree, [])
sol.insert(tree, 10)
sol.insert(tree, 11)
print()
sol.inorder(tree, [])
print()
sol.delete_node(tree, tree.left.right)
sol.inorder(tree, [])
print()
