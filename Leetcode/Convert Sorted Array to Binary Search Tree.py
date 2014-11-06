# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, A):
    	'''hint:step 2: BFS build the BST
    			step 3: DFS inorder to place the value'''
    	if not A:
    		return 

    	# build a root, use 0 as a value holder
    	root = TreeNode(0)

    	self.BFS(len(A), [root])
    	self.DFS(root, A)
    	return root

    def BFS(self, leng, this_level):
    	if not this_level:
    		return
    	next_level = []
    	for node in this_level:
    		if leng-1 > 0:
    			node.left = TreeNode(0)
    			next_level.append(node.left)
    			leng -=1
    		if leng-1 > 0:
    			node.right = TreeNode(0)
    			next_level.append(node.right)
    			leng -= 1
    	this_level = next_level
    	self.BFS(leng, this_level)

    def DFS(self, root, A):
    	if not root:
    		return
    	self.DFS(root.left, A)
    	root.val = A.pop(0)
    	self.DFS(root.right, A)

s = Solution()
A = [-1,0,1,2]
r = s.sortedArrayToBST(A)
def DFSS(r):
	if not r:
		return
	DFSS(r.left)
	print r.val
	DFSS(r.right)

DFSS(r)
