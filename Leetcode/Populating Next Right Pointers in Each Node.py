# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    
    # def connect(self, root):
    #     # using extra space, BFS
    #     if not root:
    #         return 
    #     this_level = [root]
    #     self.BFS(this_level)
        
    # def BFS(self, this_level):
    #     if not this_level: # exit
    #         return
    #     next_level = []
    #     for i in range(0, len(this_level)):
    #         currnode = this_level[i]
    #         if currnode.left:
    #             next_level.append(currnode.left)
    #         if currnode.right:
    #             next_level.append(currnode.right)

    #         if currnode != this_level[-1]:
    #             currnode.next = this_level[i+1]
    #             currnode = currnode.next
    #     self.BFS(next_level)
    
    def connect(self, root):
        # using constant extra space, DFS
        if not root:
            return 
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        