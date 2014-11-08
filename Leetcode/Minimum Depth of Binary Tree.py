# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        self.mindepth = 0
        self.DFS(root, 1)
        return self.mindepth
        
    def DFS(self, root, depth):
        if not root:
            return
        if not root.left and not root.right: # leaf
            if self.mindepth == 0: # first leaf
                self.mindepth = depth
            if depth < self.mindepth:
                self.mindepth = depth
        self.DFS(root.left, depth + 1)
        self.DFS(root.right, depth + 1)
        
        