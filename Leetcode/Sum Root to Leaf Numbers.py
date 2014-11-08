# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root, s = 0):
        if not root:
            return 0
        s += root.val
        if not root.left and not root.right: # leaf
            return s
        left = self.sumNumbers(root.left, s * 10)
        right = self.sumNumbers(root.right, s * 10)
        return left + right
        