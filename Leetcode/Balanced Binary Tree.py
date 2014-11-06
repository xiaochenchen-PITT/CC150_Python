# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        self.flag = True
        self.stack = []
        self.DFS(root, 1)
        return self.flag
        
    def DFS(self, root, depth):
        if not root:
            return
        if not(root.left and root.right):
            if depth not in self.stack:
                self.stack.append(depth)
            else:
                for each in self.stack:
                    if depth - each > 1:
                        self.flag = False
                    else:
                        self.stack.append(depth)
        self.DFS(root.left, depth + 1)
        self.DFS(root.right, depth + 1)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print s.isBalanced(root)