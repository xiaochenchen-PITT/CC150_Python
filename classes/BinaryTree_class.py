class BinaryTree:
    """BinaryTree has methods of insert and travelsal"""
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def InsertLeft(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.left = self.left
            self.left = t

    def InsertRight(self,data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.right = self.right
            self.right = t

    # DFS Travelsal methods
    def PreOrder(self, root):
        if root:
            print root.data,
            self.PreOrder(root.left),
            self.PreOrder(root.right),
        else:
            return 

    def InOrder(self, root):
        if root:
            self.InOrder(root.left),
            print root.data,
            self.InOrder(root.right),
        else:
            return

    def PostOrder(self, root):
        if root:
            self.PostOrder(root.left),
            self.PostOrder(root.right),
            print root.data,
        else:
            return

    # The key point of Iterative travelsal is to use a CHECK POINT!
    def PreOrder_Iter(self, root):
        queue = []
        check_points = []
        while root:
            while root:
                queue.append(root.data)
                if root.right:
                    check_points.append(root.right)
                root = root.left
            if len(check_points) == 0:
                root = None     # exit!
            else:
                root = check_points.pop()
        return queue

    def PostOrder_Iter(self, root):
        check_points = []
        stack = []  # have to go backward, so need a LIFO
        while root:
            while root:
                stack.append(root.data)
                if root.left:
                    check_points.append(root.left)
                root = root.right
            if len(check_points) == 0:
                root = None       # exit!
            else:
                root = check_points.pop()
        return stack[::-1]

    # BFS Travelsal method
    def LevelOrder(self, root, this_level = None):
        if this_level != []:
            next_level = []
            if this_level is None:
                this_level = [root]
            for node in this_level:
                print node.data,
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            this_level = next_level
            self.LevelOrder(root, this_level)
        else:
            return

    def GetDepth(self, root):
        if not root:
            return 0
        left_depth = GetDepth(root.left)
        right_depth = GetDepth(root.right)
        return max(left_depth, right_depth) + 1
    def IsBalanced(self, root):
        pass
    def LeastCommonAncester(self, root, node1, node2):
        '''Find the Least Common Ancester of node1 and node2'''
        if not root:
            return
        if root.data == node1.data or root.data == node2.data:
            return root
        l = LeastCommonAncester(root.left, node1, node2)
        r = LeastCommonAncester(root.right, node1, node2)

        if l and r:
            return root
        return l if l else r

    # find Maximum Path Sum Leetcode  
    level = 0
    solution_max = - 10**10
    def MaxPathSum(self, root):
        if root is None:
            return 0

        self.level += 1
        leftpath = self.MaxPathSum(root.left)
        rightpaht = self.MaxPathSum(root.right)
        self.level -= 1

        self.solution_max = max(self.solution_max, leftpath+rightpaht+root.data)
        if self.level == 0:
            return self.solution_max
        else:
            return max(root.data+leftpath, root.data+rightpaht, 0)

# test
if __name__ == '__main__':
    # create manually 
    root = BinaryTree(1)
    root.InsertLeft(2)
    root.InsertRight(7)
    root.left.InsertLeft(3)
    root.left.InsertRight(6)
    root.right.InsertRight(8)
    root.left.left.InsertLeft(4)
    root.left.left.InsertRight(5)


    print 'PreOrder:'
    root.PreOrder(root)
    print ''

    print 'PreOrder_Iter:'
    print root.PreOrder_Iter(root)
    print ''

    print 'InOrder:'
    root.InOrder(root)
    print ''

    print 'PostOrder:'
    root.PostOrder(root)
    print ''

    print 'PostOrder_Iter:'
    print root.PostOrder_Iter(root)
    print ''

    print 'LevelOrder:'
    root.LevelOrder(root)
    print ''
    
    print root.MaxPathSum(root)
