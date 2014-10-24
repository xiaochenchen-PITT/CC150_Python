import sys
sys.path.append('..')  # include one level parent dir
import classes.LinkedList_class

'''2.1 Write code to remove duplicates from an unsorted linked list 
FOLLOW UP:
How would you solve this problem if a temporary buffer is not allowed?
'''
# def RmDups(LinkedList):
# 	'''hint: use prev_node and keep refreshing the next of it. 
# 			 And when it comes a node with new data, change prev_node to this node'''
# 	NodeData_list = []
# 	node = LinkedList.head
# 	while node:
# 		if node.data not in NodeData_list:
# 			NodeData_list.append(node.data)
# 			prev_node = node
# 		else:	# if not, just keep refreshing the next of prev_node
# 			prev_node.next = node.next
# 		node = node.next
# 	return LinkedList

# def FollowUp(LinkedList):
# 	node = LinkedList.head
# 	while node:
# 		cmp_node = node
# 		prev_node = cmp_node
# 		while cmp_node:
# 			if cmp_node.data != node.data:
# 				prev_node = cmp_node
# 			else: # if not, just keep refreshing the next of prev_node
# 				prev_node.next = cmp_node.next
# 			cmp_node = cmp_node.next
# 		node = node.next
# 	return LinkedList

# ll = classes.LinkedList_class.LinkedList()
# ll.AddNode(3)
# ll.AddNode(3)
# ll.AddNode(7)
# ll.AddNode(5)
# ll.AddNode(3)
# ll.AddNode(3)
# ll.AddNode(4)
# ll.AddNode(7)
# ll.AddNode(8)
# ll.AddNode(5)
# # ll.AddNode(5)
# print ll

# # RmDups(ll)
# # print ll
# FollowUp(ll)
# print ll


'''2.2 Find the nth from the end of a singly linkedlist.
eg. 8->10->5->7->2->1->5->4->10->10 then the result is  7th to last node is 7
'''
# def FindNth(LinkedList, n):
# 	if n < 1:
# 		raise ValueError ('please enter a valid n.')

# 	node = LinkedList.head
# 	i = 0
# 	while node:
# 		node = node.next
# 		i += 1
# 	leng = i

# 	if n > leng:
# 		raise ValueError ('n is larger than length')

# 	m = leng - n + 1 # nth from the end is the mth from the start
# 	i = 1
# 	node = LinkedList.head
# 	while i < m:
# 		node = node.next
# 		i += 1
# 	return node.data

# ll = classes.LinkedList_class.LinkedList()
# ll.AddNode(3)
# ll.AddNode(3)
# ll.AddNode(7)
# ll.AddNode(5)
# ll.AddNode(3)
# ll.AddNode(3)
# ll.AddNode(4)
# ll.AddNode(7)
# ll.AddNode(8)
# ll.AddNode(5)
# print FindNth(ll, 4)

'''2.3 Implement an algorithm to delete a node in the middle of a single 
linked list, given only access to that node.
EXAMPLE:
Input: the node 'c' from a->b->c->d->e
Result: nothing is returned, but the new linked list is a->b->d->e
'''
def DelMiddle(mid_node):
	'''Consider: what if the middle node is the only node? Discuss with the interviewer!'''
	if mid_node is None or mid_node.next is None:
		raise Exception (LinkedList)

	mid_node.data = mid_node.next.data # simply copy the data, and modify .next
	mid_node.next = mid_node.next.next


'''2.4 You have two numbers represented by a linked list, where each node contains a 
single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and 
returns the sum as a linked list.
EXAMPLE:
input: (3->1->5), (6->9->2)
Output:9->0->8
'''
# def AddList(LinkedList1, LinkedList2, carry = 0):
# 	node_list = []
# 	DFS(LinkedList1.head, LinkedList2.head, 0, node_list)
# 	new_l = classes.LinkedList_class.LinkedList()
# 	node = new_l.head
# 	while node_list:
# 		new_l.AddNode(node_list.pop(0))
# 	return new_l

# def DFS(node1, node2, carry, node_list):
# 	if node1 is None and node2 is None:
# 		return

# 	val = carry
# 	if node1:
# 		val += node1.data
# 	if node2:
# 		val += node2.data

# 	if val > 9:
# 		val = val - 10
# 		carry = 1
# 	else:
# 		carry = 0

# 	node_list.append(val)
# 	DFS(node1.next if node1 else None, node2.next if node2 else None, carry, node_list)
# 	return node_list

# ll1 = classes.LinkedList_class.LinkedList()
# ll2 = classes.LinkedList_class.LinkedList()

# ll1.AddNode(3)
# ll1.AddNode(1)
# ll1.AddNode(5)

# ll2.AddNode(6)
# ll2.AddNode(9)
# ll2.AddNode(2)
# ll2.AddNode(1)

# print AddList(ll1, ll2)

'''2.5 Given a circular linked list, returns node at the beginning of the loop
EXAMPLE:
Input: A->B->C->D->E->C
Output: C
'''
# def FindBeginning(LinkedList):
# 	node = LinkedList.head
# 	# mapp = {} # key: nodes, value: 0 / 1 as visited or not
# 	visited_list = []
# 	while node:
# 		if node not in visited_list:
# 			# mapp[node] = 0 # 0: unvisited, 1: visited
# 			visited_list.append(node)
# 		else:
# 			break
# 		node = node.next
# 	return node.data

# ll = classes.LinkedList_class.LinkedList()
# ll.AddNode(1)
# ll.AddNode(2)
# ll.AddNode(3)
# t_node = ll.current_node
# ll.AddNode(4)
# ll.AddNode(5)
# ll.current_node.next = t_node

# print FindBeginning(ll)






