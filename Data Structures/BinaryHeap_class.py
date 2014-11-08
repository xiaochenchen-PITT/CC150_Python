class BinaryHeap:
	"""class BinaryHeap has Add, Remove and IsEmpty methods.
	It is implemented using list.

	To look for:

	leftchild: 2*i + 1
	rightchild: 2*i + 2
	parent: (i - 1) / 2"""

	def __init__(self):
		self.heap = []
		self.currSize = 0

	def heaplify(self, i): # mostly used in Add() and Del().
		starting = i 		# __ infront means it is private to this class
		while i > 0: 
			if self.heap[i] < self.heap[(i-1)/2]: # this is a minHeap
				t = self.heap[(i-1)/2]
				self.heap[(i-1)/2] = self.heap[i]
				self.heap[i] = t
				i = starting
				continue
			i = i - 1

	def Add(self, data):
		self.heap.append(data)
		self.currSize += 1
		self.heaplify(self.currSize-1)

	def Del(self, data):
		self.heap.remove(data)
		self.currSize -= 1
		self.heaplify(self.currSize-1)

	def Pop(self):
		self.currSize -= 1
		self.popout = self.heap.pop(0)
		self.heaplify(self.currSize-1)
		return self.popout

# test
if __name__ == '__main__':
	h = BinaryHeap()
	h.Add(5)
	h.Add(2)
	h.Add(7)
	h.Add(6)
	h.Add(4)
	h.Add(3)
	h.Add(1)

	print h.heap

	h.Del(1)
	print h.heap

	print h.Pop()
	print h.heap
	