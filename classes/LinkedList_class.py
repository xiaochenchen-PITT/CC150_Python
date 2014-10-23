class Node:
	"""docstring for Node."""
	def __init__(self, data = None, next = None):
		self.data = data	
		self.next = next

class LinkedList:
	"""This LinkedList has AddNode, DelNode, InsertNode in_place Qsort and GetLeng methods."""
	def __init__(self):
		self.current_node = Node()
		self.head = Node()
		# self.tail = Node()

	def __str__(self):
		"""Return a str(list) that contains data in order."""
		data_list = []
		indexing_node = self.head
		while indexing_node:
			data_list.append(indexing_node.data)
			indexing_node = indexing_node.next

		return str(data_list)

	def AddNode(self, data):
		new_node = Node(data, None)	

		if self.head.data:  # if not empty
			self.current_node.next = new_node
			self.current_node = new_node
		else:
			self.head = new_node
			self.current_node = new_node

	def DelNode(self, data):
		'''Delete the node with data.'''
		indexing_node = self.head
		while indexing_node.next:
			if indexing_node.next.data == data:
				indexing_node.next = indexing_node.next.next
				break
			indexing_node = indexing_node.next
		else:
			print 'No data found!'
			raise ValueError(data)

	def InsertNode(self, data, data_new): 
		'''Insert one node after the node with data.'''
		indexing_node = self.head
		while indexing_node.next:  # if not last one
			if indexing_node.data == data:
				new_node = Node(data_new, None)
				new_node.next = indexing_node.next
				indexing_node.next = new_node
				break
			indexing_node = indexing_node.next
		else:
			print 'No data found!'
			raise ValueError(data)

	def GetLeng(self):
		indexing_node = self.head
		i = 1
		while indexing_node.next:
			i += 1
			indexing_node = indexing_node.next
		return i

	def Sort(self):
		'''Inplace interchange the data'''
		data_list = []
		indexing_node = self.head
		while indexing_node:
			data_list.append(indexing_node.data)
			indexing_node = indexing_node.next

		def partition(data_list, left, right):
			pivot = data_list[right]
			for i in xrange(left, right):
				if data_list[i] < pivot:
					data_list[left], data_list[i] = data_list[i], data_list[left]
					left += 1
			data_list[left], data_list[right] = data_list[right], data_list[left]
			return left

		def qsort(data_list, left, right):
			if left < right:
				new_pivot = partition(data_list, left, right)
				qsort(data_list, left, new_pivot-1)
				qsort(data_list, new_pivot+1, right)
				return data_list

		sorted_data_list = qsort(data_list, 0, len(data_list)-1)

		indexing_node = self.head
		i = 0
		while indexing_node:
			indexing_node.data = sorted_data_list[i]
			i += 1
			indexing_node = indexing_node.next

	def Reverse(self):
		'''Reverse the Single LinkedList'''
		node = self.head
		node_list = [node]
		while node.next:
			node_list.append(node.next)
			node = node.next

		self.head = node
		while len(node_list) > 0:
			node.next = node_list.pop()
			node = node.next
		node.next = None


# test
if __name__ == '__main__':
	ll = LinkedList()
	ll.AddNode(3)
	ll.AddNode(7)
	ll.AddNode(5)
	ll.InsertNode(3, 4)

	print ll

	ll.Reverse()
	print ll
	# print ll.GetLeng()

	# ll.DelNode(4)

	# print ll
	# print ll.GetLeng()

	# ll.Sort()
	# print ll





