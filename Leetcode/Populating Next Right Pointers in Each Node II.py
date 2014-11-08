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
    #     # this ugly piece of code should have passed, but I can't figure out why it didn't...
    #     if not root:
    #         return
    #     if root.left and root.right:
    #         root.left.next = root.right
    #         node = root
    #         while node.next:
    #             if node.next.left:
    #                 root.right.next = node.next.left
    #                 break
    #             elif node.next.right:
    #                 root.right.next = node.next.right
    #                 break
    #             else:
    #                 node = node.next
    #     else:
    #         if root.left:
    #             node = root
    #             while node.next:
    #                 if node.next.left:
    #                     root.left.next = node.next.left
    #                     break
    #                 elif node.next.right:
    #                     root.left.next = node.next.right
    #                     break
    #                 else:
    #                     node = node.next
    #         if root.right:
    #             node = root
    #             while node.next:
    #                 if node.next.left:
    #                     root.right.next = node.next.left
    #                     break
    #                 elif node.next.right:
    #                     root.right.next = node.next.right
    #                     break
    #                 else:
    #                     node = node.next
    #     self.connect(root.left)
    #     self.connect(root.right)
        
    def connect(self, root):
        # use generator to mimic BFS, also solved extra space problem
        if not root:
            return
        ChildGenerator = self.ChildGen(root)
        left_most = ChildGenerator.next()
        node = left_most
        while node: # this is the while loop 1!
            node.next = ChildGenerator.next()
            node = node.next
        self.connect(left_most)
        
    def ChildGen(self, root):
        while root:
            if root.left:
                yield root.left
            if root.right:
                yield root.right
            root = root.next
        yield None # this None is used for killing the while loop 1
            
        