class DLLNode:
	"""DLLNode stands for Double LinkedList Node"""
	def __init__(self, data = None):
		self.data = data
		self.next = None
		self.prev = None

class DoubleLinkedList:
	"""DoubleLinkedList class has Insert, Delete, Reverse methods"""
	def __init__(self):
		self.head = DLLNode()
		self.tail = DLLNode()

	def Insert(self, data):
		node = DLLNode(data)
		if not self.head.data:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node

	def Delete(self, data):
		node = self.head
		while node:
			if node.data == data:
				node.prev.next = node.next
				node.next.prev = node.prev
				return
			node = node.next
		raise ValueError ('No Key Found!')

	def Reverse(self):
		node = self.head
		while node:
			t_node = node.next
			node.next = node.prev
			node.prev = t_node
			node = node.prev	
		t_node = self.head
		self.head = self.tail
		self.tail = t_node

	def PrintDLL(self):
		self.result = []
		node = self.head
		# node = self.tail
		while node:
			self.result.append(node.data)
			node = node.next
			# node = node.prev
		return self.result

if __name__ == '__main__':
	dll = DoubleLinkedList()
	dll.Insert(2)
	dll.Insert(4)
	dll.Insert(8)
	dll.Insert(5)
	print dll.PrintDLL()

	dll.Delete(4)
	print dll.PrintDLL()

	dll.Insert(7)
	print dll.PrintDLL()
	dll.Reverse()
	print dll.PrintDLL()





		