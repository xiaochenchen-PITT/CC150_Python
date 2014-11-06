# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    
    def preorderTraversal(self, root):
        # iterative
        stack = []
        preorder = []
        while stack or root:
            if root:
                preorder.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return preorder
    
    # def preorderTraversal(self, root):
    #     # recursive
    #     self.res = []
    #     self.DFS(root)
    #     return self.res
        
    # def DFS(self, root):
    #     if not root:
    #         return 
    #     self.res.append(root.val)
    #     self.DFS(root.left)
    #     self.DFS(root.right)
            
        