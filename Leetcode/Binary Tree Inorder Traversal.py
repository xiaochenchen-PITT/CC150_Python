# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    
    def inorderTraversal(self, root):
        # iterative
        stack = []
        inorder = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inorder.append(root.val)
                root = root.right
        return inorder
        
    # def inorderTraversal(self, root):
    #     # recursive
    #     res = []  # Note here it does not need to be self.res, because it is not backtracking
    #     self.DFS(root, res)
    #     return res
        
    # def DFS(self, root, res):
    #     if not root:
    #         return 
    #     self.DFS(root.left, res)
    #     res.append(root.val)
    #     self.DFS(root.right, res)