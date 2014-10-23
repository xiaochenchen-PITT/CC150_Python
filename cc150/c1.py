'''1.1 Implement an algorithm to determine if a string has all unique character
What if you can not use additional data structures?'''

def solution(s):
# # 	for each in s:
# # 	 	if s.count(each) > 1:
# # 	 		return False	
# # 	return True
	
# 	# if count()is not allowed,
# 	# then we can sort (quick or merge) the list and then compare the 
# 	# adjacent element in the sorted list	

	# Quick Sort
	def qsort(lst):
		if len(lst) <= 1:
			return lst
		else:
			pivot = lst[0]
			less = []     # what if you can not use additional
			equal = []	  #data structure?  -- In place quick sort
			greater = []

			for each in lst:
				if each < pivot:
					less.append(each)
				elif each == pivot:
					equal.append(each)
				else:
					greater.append(each)
			return qsort(less) + equal + qsort(greater)


    # In-place quick sort (NO additional space)
	def partition(lst, left, right):
		pivot = right
		for i in xrange(left, right):
			if lst[i] < lst[pivot]:
				lst[i], lst[left] = lst[left],lst[i]
				left += 1
		lst[left], lst[right] = lst[right], lst[left]
		return left

	def inplace_qsort(lst, left, right):
		if right > left:
			new_pivot = partition(lst, left, right)
			inplace_qsort(lst, left, new_pivot-1)
			inplace_qsort(lst, new_pivot+1, right)
			return lst


	# Merge Sort
	def msort(lst):

		def merge(left, right):
			merged_list = []
			while left and right:
				if left[0] <= right[0]:
					merged_list.append(left.pop(0))
				else:
					merged_list.append(right.pop(0))
			while left:
				merged_list.append(left.pop(0))
			while right:
				merged_list.append(right.pop(0))
			return merged_list

		if len(lst) <= 1:	
			return lst
		else:
			middle_index = len(lst) / 2
			left = msort(lst[:middle_index])
			right = msort(lst[middle_index:])
			return merge(left, right)

	# sorted_list = qsort(list(s))
	# sorted_list = inplace_qsort(list(s), 0, len(s)-1)
	sorted_list = msort(list(s))
	print sorted_list
	for i in xrange(0, len(sorted_list)-1):
		if sorted_list[i] == sorted_list[i+1]:
			return False
	return True

string = "af.sdvs"
print solution(string)

'''1.2 Write code to reverse a C-Style String 
(C-String means including the null character at the end)'''

def solution(s):
	return s[::-1]

string = "bdvir"
print solution(string)

'''1.3 Design an algorithm and write code to remove the duplicate characters 
in a string without using any additional buffer
NOTE: One / two additional variables are fine An extra copy of the array is not
'''
def solution(a):
# In place quick sort the string and check the adjacent element 
# and remove the same one.

	if len(a) <= 1:
		return a

	def partition(a, left, right):
		pivot = right
		for i in xrange(left, right):
			if a[i] < a[pivot]:
				a[left], a[i] = a[i], a[left]
				left += 1
		a[left], a[right] = a[right], a[left]
		return left

	def inplace_qsort(a, left, right):
		if right > left:
			new_pivot = partition(a, left, right)
			inplace_qsort(a, left, new_pivot-1)
			inplace_qsort(a, new_pivot+1, right)
			return a

	sorted_list = inplace_qsort(a, 0, len(a)-1)
	print sorted_list
	i = 0
	while i < len(sorted_list)-1:			# Note: this is how you do when you
		if sorted_list[i] == sorted_list[i+1]:# try to delete some elements from
			sorted_list.pop(i)		      # the list (plz don't use for loop!!!)
			continue
		i += 1
	return sorted_list

# l = [1,2,3,7,3,9,2,7]
l = [1,2,3,2]
print solution(l)
	
def solution(lst): #if not allowed to destroy the original order
	i = 0
	while i < len(lst):
		j = i + 1
		while j < len(lst):
			if lst[i] == lst[j]:
				lst.pop(j)
				continue
			j += 1
		i += 1
	return lst

s = 'davgdfverv'
print solution(list(s))

'''1.4 Write a method to tell if two strings are anagrams or not
eg. iceman vs cinema'''
def solution(s1,s2):
	l1 = list(s1)
	l2 = list(s2)
	l1.sort()  # Note: sort()method does not return anything!!!
	l2.sort()
	return l1 == l2

print solution('asd', 'dga')

'''1.5 write a method to replace all spaces in a string with "%20"
'''
def solution(s):
	return '%20'.join(s.split(" "))

print solution('haha this is china')

'''1.6 Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees Can you do this in place?
'''
# not inplace
def solution(matrix):
	if len(matrix) == 1:
		return matrix

	new_matrix = []
	for i in xrange(0,len(matrix)):
		row = []
		for j in xrange(0,len(matrix[0])):
			row.append(matrix[len(matrix)-1-j][i])
		new_matrix.append(row)
	return new_matrix

# inplace 
def solution(matrix):		 
	if len(matrix) < 2:
		return matrix
							 # idea is reverse the matrix up side down and swap
	matrix = matrix[::-1]	 # along the diagonal
	print matrix
	for i in xrange(0,len(matrix)):    # Notice: just swap the upper half!
		for j in xrange(i,len(matrix)):# Or you will get back 
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	return matrix

mat = [[1,2,3], [4,5,6], [7,8,9]]
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat = [1]			
print solution(mat)
			

"""1.7 Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column is set to 0
"""
def solution(matrix, M, N):  # M: # of rows; N: # of cols
	zero_list = []
	for i in xrange(0, M):
		for j in xrange(0, N):
			if matrix[i][j] == 0:
				zero_list.append([i, j])
	print zero_list

	for i_j_pair in zero_list:
		for x in xrange(0, N):
			matrix[i_j_pair[0]][x] = 0
		for y in xrange(0, M):
			matrix[y][i_j_pair[1]] = 0

	return matrix

mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print solution(mat, len(mat), len(mat[0]))
	

"""1.8 Assume you have a method isSubstring which checks
if one word is a substring of another. Given two strings,s1 and s2,
write code check if s2 is a rotation of s1 using only one call to isSubstring
(eg. 'waterbottle' is rotation of 'erbottlewat') 
"""
def isSubstring(s1, s2): # wether s2 is sub of s1 
	for l in xrange(0, len(s1)):
		for r in xrange(len(s1), 0, -1):
			if s1[l:r] == s2:
				return True	
	return False

def solution(s1, s2):
	if len(s1) != len(s2) or len(s1) == 0:
		return False

	s1s1 = s1+s1
	return isSubstring(s1s1, s2)

# s1 = 'waterbottle'
# s2 = 'erbottlewat'
s1 = ''
s2 = 'k'
print solution(s1, s2)



