# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root, depth = 0):
        if not root:
            return depth
        l = self.maxDepth(root.left, depth + 1)
        r = self.maxDepth(root.right, depth + 1)
        return l if l > r else r