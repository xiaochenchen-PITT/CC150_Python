import sys
sys.path.append('..')
import classes.BinaryTree_class
import classes.LinkedList_class
'''4.1 Implement a function to check if a tree is balanced 
For the purposes of this question, a balanced tree is defined to be a tree 
such that no two leaf nodes differ in distance from the root by more than one.
'''
# max_depth = 1
# flag = True
# def isBalanced(root, depth):
# 	# max_depth = 1
# 	# flag = True
# 	return DFS(root, depth)
# def DFS(root, depth):
# 	global max_depth, flag
# 	if not root:
# 		if depth - 1 < max_depth - 1:
# 			flag = False
# 			print 'flag changed!'
# 		max_depth = depth - 1 
# 		return True
# 	else:
# 		print 'node', root.data
# 		print 'depth', depth
# 		print 'max_depth', max_depth
# 		print ''
# 		DFS(root.left, depth + 1)
# 		DFS(root.right, depth + 1)
# 	return flag

# root = classes.BinaryTree_class.BinaryTree(1)
# root.InsertLeft(2)
# root.InsertRight(7)
# root.left.InsertLeft(3)
# root.left.InsertRight(6)
# root.right.InsertRight(8)
# root.left.left.InsertLeft(4)
# root.left.left.InsertRight(5)
# root.left.left.right.InsertRight(10)
# print isBalanced(root, 1)

'''4.2 Given a directed graph, design an algorithm to find out whether 
there is a route between two nodes
'''
# def FindPath(graph, start, end, path = []):
# 	path = path + [start]
# 	if start == end:
# 		return path
# 	if start not in graph:
# 		return
# 	for node in graph[start]:
# 		if node not in path:
# 			return FindPath(graph, node, end, path)

# graph = {'A':['B', 'C'],
# 		'B': ['C', 'D'],
# 		'C': ['CD'],
# 		'CD': ['D'],
# 		'D': ['C'],
# 		'E': ['F'],
# 		'F': ['C', 'G']}
# print FindPath(graph, 'A', 'D')

'''4.3 Given a sorted (increasing order) array, write an algorithm to create a 
binary tree with minimal height, return the minimal height.
'''
# class BinaryTree:
#  	def __init__(self, data, left = None, right = None):
#  		self.data = data
# 		self.left = left
# 		self.right = right

# def BinaryTreeCreation(arr):
# 	'''Hint: minimal height -> BFS'''
# 	global this_level, depth
# 	if lst:
# 		depth = 1
# 		root = BinaryTree(lst.pop())
# 		this_level = [root]
# 		return RecursiveCreation(arr)
# 	else:
# 		return 
# def RecursiveCreation(arr):
# 	global this_level, depth
# 	if this_level:
# 		next_level = []
# 		for node in this_level:
# 			if arr:
# 				node.left = BinaryTree(arr.pop())
# 				next_level.append(node.left)
# 			if arr:
# 				node.right = BinaryTree(arr.pop())
# 				next_level.append(node.right)
# 		if next_level:
# 			depth += 1
# 		this_level = next_level
# 		RecursiveCreation(arr)
# 	return depth
# lst = [1,2,3,4,5,6,7,8,9,10,11]
# print BinaryTreeCreation(lst)

'''4.4 Given a binary search tree, design an algorithm which creates a linked 
list of all the nodes at each depth.
(eg, if you have a tree with depth D, you'll have D linked lists)
'''
# def LinkedListCreation(root): # BFS
# 	global this_level, LinkedLists
# 	if root:
# 		this_level = [root]
# 		LinkedLists = []
# 		return RecursiveCreation()
# 	else:
# 		return
# def RecursiveCreation():
# 	global this_level, LinkedLists, LLists
# 	if this_level:
# 		next_level = []
# 		node_data = []
# 		LLists = []
# 		for node in this_level:
# 			node_data.append(node.data)
# 			if node.left:
# 				next_level.append(node.left)
# 			if node.right:
# 				next_level.append(node.right)
# 		# Creat LinkedList
# 		head = classes.LinkedList_class.LinkedList()
# 		head.data = node_data[0]
# 		LLists.append(head.data)
# 		current_node = head
# 		for data in [data for data in node_data if data != node_data[0]]:
# 			t_node = classes.LinkedList_class.LinkedList()
# 			t_node.data = data
# 			LLists.append(t_node.data)
# 			current_node.next = t_node
# 			current_node = t_node
# 		LinkedLists.append(LLists)
# 		this_level = next_level
# 		RecursiveCreation()
# 	return LinkedLists

# root = classes.BinaryTree_class.BinaryTree(1)
# root.InsertLeft(2)
# root.InsertRight(7)
# root.left.InsertLeft(3)
# root.left.InsertRight(6)
# root.right.InsertRight(8)
# root.left.left.InsertLeft(4)
# root.left.left.InsertRight(5)
# root.left.left.right.InsertRight(10)
# print LinkedListCreation(root)

'''4.5 Find the "next" node (in-order successor) of a given node in a 
binary tree where each node has a link to its parent
'''
# def FindNext(root, data):
# 	global inorder_list
# 	inorder_list = []
# 	# in-order traversal, get whole traversal list
# 	node_list = inorder(root)
# 	# then just get the next node rigth next to it
# 	for i in xrange(len(node_list)):
# 		if node_list[i] == data:
# 			return node_list[i+1]
# def inorder(root):
# 	global inorder_list
# 	if not root:
# 		return 
# 	inorder(root.left)
# 	inorder_list.append(root.data)
# 	inorder(root.right)
# 	return inorder_list

# root = classes.BinaryTree_class.BinaryTree(1)
# root.InsertLeft(2)
# root.InsertRight(7)
# root.left.InsertLeft(3)
# root.left.InsertRight(6)
# root.right.InsertRight(8)
# root.left.left.InsertLeft(4)
# root.left.left.InsertRight(5)
# root.left.left.right.InsertRight(10)
# print FindNext(root, 6)

'''4.6 Find the first common ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
'''
# def FindLCA(root, node1, node2):
# 	if not root:
# 		return

# 	if root.data == node1.data or root.data == node2.data:
# 		return root.data
# 	else:
# 		l = FindLCA(root.left, node1, node2)
# 		r = FindLCA(root.right, node1, node2)

# 	if l and r:
# 		return root.data
# 	if l:
# 		return l
# 	if r:
# 		return r
# 	return

# root = classes.BinaryTree_class.BinaryTree(1)
# root.InsertLeft(2)
# root.InsertRight(7)
# root.left.InsertLeft(3)
# root.left.InsertRight(6)
# root.right.InsertRight(8)
# root.left.left.InsertLeft(4)
# root.left.left.InsertRight(5)
# print FindLCA(root, root.left.left.right, root.left.right)



		









