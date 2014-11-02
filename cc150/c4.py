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


'''4.7 You have two very large binary trees: T1, with millions of nodes, 
and T2, with hundreds of nodes Create an algorithm to decide if T2 is 
a subtree of T1
'''
# def IsSub(node1, node2): # node1 is big tree, node2 is small tree
# 	if not node2: # empty tree is always a subtree
# 		return True
# 	return IsSub_recur(node1,node2)

# def IsSub_recur(node1, node2):
# 	if not node1: # exit, node1 reaches the leaf but still no match
# 		return False
# 	if node1.data == node2.data: # found a match, go check wether each following nodes match 
# 		return IsMatch(node1, node2)
# 	# Recursively go along tree 1 and check for match
# 	return (IsSub_recur(node1.left, node2) or IsSub_recur(node1.right, node2))

# def IsMatch(node1, node2):
# 	if not node1 and not node2:
# 		return True
# 	if not node1 or not node2: 
# 		return False
# 	if node1.data == node2.data:
# 		return (IsMatch(node1.left, node2.left) or IsMatch(node1.right, node2.right))
# 	else:
# 		return False
# If it is not this big(millions of nodes...), we can record the in-order and pre-order
# of both tree1 and tree2, and check whether one is the substrings of the other.

'''4.8 You are given a binary tree in which each node contains a value. 
Design an algorithm to print all paths which sum up to that value. 
Note that it can be any path in the tree - it does not have to start at the root.
'''
# def FindSumPath(root, target, path = []):
# 	'''define path : only going towards leaf'''
# 	if not root:
# 		return
# 	path.append(root.data)
# 	# print 'root, path', root.data, path

# 	s = 0
# 	i = 0
# 	for node_data in path[::-1]:
# 		s += node_data
# 		i += 1 # i is for restricting the end of printing elements in path
# 		if s == target:
# 			PrintThisPath(path, i)
# 	FindSumPath(root.left, target, path)
# 	FindSumPath(root.right, target, path)
# 	path.pop()	

# def PrintThisPath(path, i):
# 	path_new = path[::-1]
# 	for node in path_new[:i]:
# 		print node,
# 	print ''

# root = classes.BinaryTree_class.BinaryTree(1)
# root.InsertLeft(2)
# root.InsertRight(7)
# root.left.InsertLeft(3)
# root.left.InsertRight(6)
# root.right.InsertRight(8)
# root.left.left.InsertLeft(4)
# root.left.left.InsertRight(5)
# root.left.left.right.InsertRight(10)

# FindSumPath(root, 21)

