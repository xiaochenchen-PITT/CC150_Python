# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root:
            return []
        this_level = [root]
        self.stack = [] # LIFO
        self.BFS(this_level)
        print 'self.stack', self.stack
        return self.stack[::-1]
        
    def BFS(self, this_level):
        if this_level:
            next_level = []
            for node in this_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            self.stack.append([node.val for node in this_level])
            self.BFS(next_level)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print s.levelOrderBottom(root)
        