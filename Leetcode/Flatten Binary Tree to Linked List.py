# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    
    # def flatten(self, root):
    #     # not in place
    #     # use stack to store the preorder traversal, the build a flatten tree using it
    #     if not root:
    #         return 
    #     self.preorders = []
    #     self.DFS(root)
    #     nodes = self.preorders
    #     self.buildTree(root, nodes)
        
    # def DFS(self, root):
    #     if not root:
    #         return
    #     self.preorders.append(root)
    #     self.DFS(root.left)
    #     self.DFS(root.right)
        
    # def buildTree(self, root, nodes):
    #     for node in nodes[1:]:
    #         root.right = node
    #         root = root.right
        
    # def flatten(self, root):
    #     # in place
    #     # iterative
    #     if not root:
    #         return 
    #     while root:
    #         if root.left:
    #             if root.right:
    #                 rightmost = root.left
    #                 while rightmost.right: # finding the rightmost of the left subtree of this root
    #                     rightmost = rightmost.right
    #                 rightmost.right = root.right
    #             root.right = root.left
    #             root.left = None
    #         root = root.right
        
    def flatten(self, root):
        # "in-place" 
        # recursive (actually, recursive method is not strictly in-place 
        # since it need a stack to store the argument and return addr)
        if not root:
            return
        dummy = TreeNode(32)
        dummy.right = root
        self.prev = dummy # prev is used for tracking previous node (pre-order)
        self.preorder(root)
        
    def preorder(self, root):
        if not root:
            return 
        
        self.prev.right = root
        self.prev.left = None
        self.prev = root
        
        rightNode = root.right
        self.preorder(root.left)
        self.preorder(rightNode)
        
        
        
        