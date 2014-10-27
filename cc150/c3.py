'''3.1 Describe how you could use a single array to implement three stacks
'''
# class SingleArrayStack:
# 	"""The Array (list) is divided into 3 parts evenly."""
# 	def __init__(self, stacksize = 100, number = 3):
# 		self.stacksize = stacksize
# 		self.number = number
# 		self.array = [None] * self.stacksize * self.number
# 		self.sp = [0] * self.number

# 	def push(self, data, number): #0 stack, #1 stack, #2 stack...
# 		if self.sp[number] + 1 > self.stacksize: #out of stack
# 			raise exception ('Out of Stack!')

# 		self.array[stacksize * number + sp[number]] = data
# 		self.sp[number] += 1

# 	def pop(self, number):
# 		if self.sp[number] < 0:
# 			raise exception ('Pop from empty stack!')

# 		dada = self.array([stacksize * number + sp[number]])
# 		self.array[stacksize * number + sp[number]] = None
# 		self.sp[number] -= 1
# 		return data

# 	def isempty(self, number):
# 		if self.sp[number] == -1:
# 			return True
# 		return False

'''3.2 How would you design a stack which, in addition to push and pop, also has a 
function min which returns the minimum element? Push, pop and min should 
all operate in O(1) time.
'''
# class StackwithMin:
# 	"""Approach one, using a tuple to store the current min in each element"""
# 	def __init__(self):
# 		self.stack = []

# 	def push(self, data):
# 		'''Assume the stack has unlimited size.'''
# 		if len(self.stack) == 0:
# 			self.stack.append((data, data))
# 		else:
# 			curr_min = self.stack[-1][-1]
# 			if curr_min < data:
# 				self.stack.append((data, curr_min))
# 			else:
# 				self.stack.append((data,data))

# 	def pop(self):
# 		if len(self.stack) == 0:
# 			raise Exception ('Pop from empty stack!')
# 		return self.stack.pop()[0]

# 	def Findmin(self):
# 		if len(self.stack) == 0:
# 			return
# 		return self.stack[-1][-1]


# class StackwithMin2:
# 	"""Approach two, using a list to keep track of the minimum."""
# 	def __init__(self):
# 		self.stack = []
# 		self.min_stack = []

# 	def push(self, data):
# 		'''Assume the stack has unlimited size.'''
# 		if len(self.stack) == 0:
# 			self.stack.append(data)
# 			self.min_stack.append(data)
# 		else:
# 			self.stack.append(data)
# 			if data < self.min_stack[-1]:
# 				self.min_stack.append(data)	

# 	def pop(self):
# 		if len(self.stack) == 0:
# 			raise Exception ('Pop from empty stack!')
# 		if self.stack[-1] == self.min_stack[-1]:
# 		 	self.min_stack.pop()
# 		return self.stack.pop()
		 
# 	def Findmin(self):
# 		if len(self.stack) == 0:
# 			return None
# 		return self.min_stack[-1]

# s = StackwithMin2()
# s.push(5)
# s.push(3)
# s.push(9)
# s.push(1)
# s.push(8)

# print s.Findmin()

# s.pop()
# a = s.pop()

# print a
# print s.Findmin() 

'''3.3 Implement a OverStack class to mimic the real-life feature of a stack, 
meaning: if it exceeds the capacity of the current stack, get a new one to keep
storing element.
'''
# class SetofStack:
# 	def __init__(self, capacity):
# 		self.capacity = capacity
# 		self.stack_set = []
# 		self.current_stack = []

# 	def push(self, data):
# 		if len(self.current_stack) == self.capacity:
# 			self.stack_set.append(self.current_stack)
# 			self.current_stack = []
# 			self.current_stack.append(data)
# 		else:
# 			self.current_stack.append(data)

# 	def pop(self):
# 		if len(self.stack_set) == 0 and len(self.current_stack) == 0:
# 			raise Exception ('Pop from empty Stack!')

# 		if len(self.current_stack) == 0:
# 			self.current_stack = self.stack_set.pop()
# 			return self.current_stack.pop()
# 		else:
# 			return self.current_stack.pop()

# s = SetofStack(3)
# for x in xrange(1,8):
# 	s.push(x)

# print s.stack_set
# print s.current_stack

# for y in xrange(1,6):
# 	print s.pop()
	
'''3.4 Towers of Hanoi
you have 3 rods and N disks of different sizes which can slide onto any tower 
The puzzle starts with each disk sitting on top of an even larger one.
(A) Only one disk can be moved at a time
(B) A disk is slid off the top of one rod onto the next rod
(C) A disk can only be placed on top of a larger disk
Write a program to move the disks from the first rod to the last using Stacks.
'''
# def Hanoi(n):
# 	rod1 = [n - i for i in xrange(n)] # [4,3,2,1]
# 	rod2 = []
# 	rod3 = []
# 	PlayHanoi(rod1, rod2, rod3, n)
# 	print rod1
# 	print rod2
# 	print rod3

# def PlayHanoi(rod1, rod2, rod3, size):
# 	if size == 1:
# 		rod3.append(rod1.pop())
# 	else:
# 		PlayHanoi(rod1, rod2, rod3, size - 1)
# 		PlayHanoi(rod3, rod1, rod2, size - 1)
# 		PlayHanoi(rod1, rod2, rod3, 1)
# 		PlayHanoi(rod2, rod1, rod3, size - 1)

# Hanoi(8)

'''3.5 Implement a MyQueue class which implements a queue using two stacks
hint: push to the first stack, and then pop it out and push to 
	  the second stack immediately. LIFO -> FIFO
'''
# class MyQueue:
# 	"""A queue using two stacks"""
# 	def __init__(self):
# 		self.stack1 = []
# 		self.stack2 = []

# 	def inqueue(self, data):
# 		if not self.stack2:
# 			self.stack2.append(data)
# 		else:
# 			self.stack1 = []
# 			while self.stack2:
# 				self.stack1.append(self.stack2.pop())
# 			self.stack1.append(data)
# 			while self.stack1:
# 				self.stack2.append(self.stack1.pop())

# 	def dequeue(self):
# 		if not self.stack2:
# 			raise IndexError('Dequeue from an empty queue!')
# 		return self.stack2.pop()

# q = MyQueue()
# for x in xrange(1, 4):
# 	q.inqueue(x)
# print q.stack2
# for x in xrange(1,4):
# 	print q.dequeue()

'''3.6 Write a program to sort a stack in ascending order. 
The following are the only functions that should be used to write this program: 
push | pop | peek(see the top most one) | isEmpty
'''
class Stack:
	"""stack has push, pop, peek and isEmpty"""
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		if len(self.stack) == 0:
			raise IndexError('Pop from Empty stack!')
		return self.stack.pop()

	def peek(self):
		"""peek the top most element"""
		return self.stack[-1]

	def isEmpty(self):
		if self.stack:
			return False
		return True

def SortStack(stack): # Pay attention to list and stack object...
	new_stack = Stack()
	while not stack.isEmpty():
		t = stack.pop()
		while (not new_stack.isEmpty()) and (new_stack.peek() > t):
			stack.push(new_stack.pop())
		new_stack.push(t)
	return new_stack.stack

s = Stack()
s.push(5)
s.push(2)
s.push(1)
s.push(4)
print SortStack(s)



		


