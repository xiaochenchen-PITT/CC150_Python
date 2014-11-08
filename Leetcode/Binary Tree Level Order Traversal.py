# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        self.res = [[root.val]]
        self.BFS([root])
        return self.res
        
    def BFS(self, this_level):
        if this_level:
            next_level = []
            for node in this_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                self.res.append([node.val for node in next_level])
            self.BFS(next_level)