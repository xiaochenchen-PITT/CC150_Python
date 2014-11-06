'''Balanced Binary Tree Definition 2:
The depth of the two subtrees of every node never differ by more than 1.'''
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
    	if not root:
    		return True
    	l = self.GetDepth(root.left, 1)
    	r = self.GetDepth(root.right, 1)
    	if abs(l - r) > 1:
    		return False
    	left = self.isBalanced(root.left)
    	right = self.isBalanced(root.right)
    	return left and right

    def GetDepth(self, root, depth):
    	if not root:
    		return depth - 1
    	l = self.GetDepth(root.left, depth + 1)
    	r = self.GetDepth(root.right, depth + 1)
    	return l if l > r else r
