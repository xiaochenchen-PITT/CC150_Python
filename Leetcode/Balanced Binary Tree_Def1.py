'''Balanced Binary Tree Definition 1:
no 2 leaf nodes differ in distance from the root by more than 1'''
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
    	self.depths = []
    	self.flag = True
    	return self.DFS(root, 1)

    def DFS(self, root, depth):
    	if not root:
    	    if not self.depths:
    	        self.depths.append(depth-1)
            else:
                for each in self.depths:
                    if abs(depth-1-each) > 1:
                        self.flag = False
                if self.flag:
                    self.depths.append(depth-1)
            return self.flag
        self.DFS(root.left, depth + 1)
        self.DFS(root.right, depth + 1)
        return self.flag