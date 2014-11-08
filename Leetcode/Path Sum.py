# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum, pathsum = 0):
        # '''key point is to be identify the leaf correctly--not root.left and not root.right'''
        if not root:
            return False
        pathsum += root.val
        if not root.left and not root.right: # leaf
            if pathsum == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum, pathsum) or self.hasPathSum(root.right, sum, pathsum)
