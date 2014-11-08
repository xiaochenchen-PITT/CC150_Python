class Queue:
	"""Queue is a FIFO strcture.
	It has Enqueue, Dequeue IsEmpty and GetSize methods."""
	def __init__(self):
		self.queue = []

	def Enqueue(self, data):
		self.queue.append(data)

	def Dequeue(self):
		self.queue.pop(0)

	def GetSize(self):
		return len(self.queue)

	def IsEmpty(self):
		if self.queue == []:
			return True
		return False

class PriorityQueue:
	"""PriorityQueue implemented by a dictionary.

	However, a PriorityQueue is more commonly implemented by a Heap.
	Please refer to Heap.class"""
	def __init__(self):
		self.pri_queue= {}

	def Insert_with_priority(self, priority, data):
		self.pri_queue[priority] = data   # key: priority, value: data

	def Pull_highest_priority_element(self):
		highest = self.pri_queue.keys()[0]
		for pri, data in self.pri_queue.items():
			if pri > highest:
				highest = pri
		pop = self.pri_queue[highest]
		del self.pri_queue[highest]
		return pop

# test
if __name__ == '__main__':
	q = Queue()
	q.Enqueue(3)
	q.Enqueue(5)
	q.Enqueue(29)
	print q.queue
	print q.GetSize()

	pq = PriorityQueue()
	pq.Insert_with_priority(1, 5)
	pq.Insert_with_priority(8, 3)
	pq.Insert_with_priority(3, 4)
	print pq.pri_queue
	print pq.Pull_highest_priority_element()
	print pq.pri_queue

