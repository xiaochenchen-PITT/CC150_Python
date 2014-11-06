# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        root_left = root.left
        root_right = root.right
        return self.DFS(root_left, root_right)
        
    def DFS(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        l = self.DFS(root1.left, root2.right)
        r = self.DFS(root1.right, root2.left)
        return l and r