# from BinaryHeap_class import BinaryHeap
from BinaryHeap_class import *

class PriorityQueue(BinaryHeap):
	"""PriorityQueue is less useful than BinaryHeap.

	Or if you really need a PriorityQueue, 
	it can be easily implemented using a dictionary."""
	def __init__(self):
		BinaryHeap.__init__(self)

	def push(self, data):
		self.heap.append(data)
		self.currSize += 1
		BinaryHeap.heaplify(self, self.currSize-1)

	def pop(self):
		self.currSize -= 1
		self.popout = self.heap.pop(0)
		self.heaplify(self.currSize-1)
		return self.popout

p = PriorityQueue()
p.push(8)
p.push(5)
p.push(7)
p.push(6)
p.push(4)
p.push(2)
p.push(3)
p.push(1)

print p.heap

p.pop()
print p.heap