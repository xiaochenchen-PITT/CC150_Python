# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    
    # def postorderTraversal(self, root):
    #     # recursive 1
    #     self.res = []
    #     self.DFS(root)
    #     return self.res
        
    # def DFS(self, root):
    #     if not root:
    #         return
    #     self.DFS(root.left)
    #     self.DFS(root.right)
    #     self.res.append(root.val)
    
    # def postorderTraversal(self, root):
    #     # recursive 2
    #     if not root:
    #         return []
    #     left = self.postorderTraversal(root.left)
    #     right = self.postorderTraversal(root.right)
    #     return left + right + [root.val]
    
    def postorderTraversal(self, root):
        # iterative 1
        if not root:
            return []
        res = []
        stack = [root] # store the parent nodes
        while stack:
            node = stack[-1]
            if node.left and node.left not in res:
                stack.append(node.left)
            elif node.right and node.right not in res:
                stack.append(node.right)
            else:
                res.append(node)  # note: res.append(node.val) can not pass...
                stack.pop()
        return [node.val for node in res]
    
    # def postorderTraversal(self, root):
    #     # iterative 2
    #     if not root:
    #         return []
    #     res = []
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node: # not None 
    #             if type(node) is int:
    #                 res.append(node)
    #             else:
    #                 stack.append(node.val)
    #                 stack.append(node.right)
    #                 stack.append(node.left)
    #     return res