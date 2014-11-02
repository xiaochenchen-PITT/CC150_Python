# #Single Number
# class Solution:
#     # @param A, a list of integer
#     # @return an integer
#     def singleNumber(self, A):
#         result = 0
#         if len(A) == 1:
#             return A[0]
#         else:
#             for each in A:               
#                 result = result ^ each  
#             return result
                    

# A = [2,2,1]

# solution = Solution()
# print solution.singleNumber(A)


# #Reverse Words in a String 
# class Solution:
#     # @param s, a string
#     # @return a string
#     def reverseWords(self, s):
#         s_reverse = []
#         s_split = s.split() 
        
#         if s_split == []:
#         	return ''
#         elif len(s_split) == 1:
#         	return s_split[0]
#         else:
#         	while s_split != []:
# 	            s_reverse.append(s_split.pop(-1))
# 	        reversed_str = ' '.join(s_reverse)
# 	        return reversed_str

# s = '  a  g '
# solution = Solution()
# print solution.reverseWords(s)


# #Reverse Integer 
# class Solution:
#     # @return an integer
#     def __init__(self,x):
#         self.x = x

#     def reverse(self):
#         reverse_list = []
#         if self.x < 0:
#             reverse_list.append('-')
#         result = abs(self.x)
#         while result >= 10:
#             reverse_list.append(str(result % 10))
#             result = result / 10 
#         reverse_list.append(str(result))
#         print reverse_list
#         return int(''.join(reverse_list))

# x = 14234000
# solution = Solution(x)
# print solution.reverse()


# class Solution:
#     # @param    A       a list of integers
#     # @param    elem    an integer, value need to be removed
#     # @return an integer
#     def removeElement(self, A, elem):
#         #A_copy = A[:]
#         for each in A:
#             if each  == elem:
#                 A.remove(each)
        
#         # print A_copy
#         return len(A)
        
# s = Solution()
# list = [1,1,23]
# print s.removeElement(list, 1)
            

# class Solution:
#     # @param A  a list of integers
#     # @param m  an integer, length of A
#     # @param B  a list of integers
#     # @param n  an integer, length of B
#     # @return nothing
#     def merge(self, A, m, B, n):
#         C = []
#         for i in A:
#             C.append(i)
#         for j in B:
#             C.append(j)
            
#         print C
        
#         for k in range(len(C)):
#             min = k
#             for elem in C[k:-1]:
#                 if C[min] > elem:
#                     min = C.index(elem)
#             temp = C[min]
#             C[min] = C[k]
#             C[k] = temp

#         print C
        

# s = Solution()
# s.merge([2,6,3,7,4,8],6,[7,3,9],3)

# # two ways to convert a decimal number into a binary number
# def convert(n):
# 	if n < 2:
# 		return n
# 	else:
# 		remain = n % 2
# 		sum = convert(n/2) * 10 + remain
# 		return sum

# print convert(13)
# print bin(13)

# # count how many 0s in a given integer
# def count(n):
#     sum = 0
#     if n < 2:
#         return 1-n
#     else:
#         sum = count(n/2) + (1-(n%2))
#     return (sum)

# print count(17)


# def find_prime(n):
#     flag = True
#     if n < 2:
#         return flag
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 flag = False
#         return flag

# print find_prime(18)


# '''Google Online Coding Assessment: 
# One was to return the numbers
# formed by interleaving the decimal digits of 2 numbers'''

# def interleave(n ,m):

# 	if (n < 10 and m < 10):
# 		return (n, m)

# 	n_list = []
# 	m_list = []

# 	n_list.append(n % 10)
# 	n = n / 10
# 	n_list.append(n % 10)
# 	n_list.append(n / 10)

# 	m_list.append(m % 10)
# 	m = m / 10
# 	m_list.append(m % 10)
# 	m_list.append(m / 10)

# 	print n_list, m_list

# 	return(n_list[2]* 100 + m_list[1] *10 + n_list[0], 
# 		   m_list[2]* 100 + n_list[1] *10 + m_list[0])


# print interleave(1234, 4567)
# print interleave(0, 9)

# '''Google Online Coding Assessment: 
# Finding Y (Y is between (min, max) of an unsorted list A[]),
# maximizing the min|(Ai-Y)|. 
# Return (Y, max of min)'''

# def finding_Y(A):
# 	# parameter A is an unsorted list
	# dict_Y_min = {}	#key: Y, value: |min(Ai-Y)|
	
	# A.sort()
	# for y in xrange(A[0],A[-1]+1):
	# 	minimum = abs(y - A[0])
	# 	for each in A:
	# 		if minimum > abs(each - y):
	# 			minimum = abs(each - y)
	# 	dict_Y_min[y] = minimum

	# print dict_Y_min

	# Y_target = dict_Y_min.keys()[0]
	# maximum = dict_Y_min.values()[0]
	# for a, b in dict_Y_min.items():
	# 	if b > maximum:
	# 		maximum = b
	# 		Y_target = a
	# return (Y_target, maximum)

# print finding_Y([1,7,2,6])

# '''Google online Coding Assessment:
# retun all the square numbers between an interval
# worst case time complexity O(N.abs(sqrt))'''

# import math
# def solution(A, B):
#     count = 0
#     for each in xrange(A, B+1):
#         if math.sqrt(each) == int(math.sqrt(each)):
#             count += 1

#     return count

# print solution(5, 9)
        
# '''Google online Coding Assessment:
# finding all local extrema(min and max) in a given list.
# worst case time camplexity is expected to be O(N)
# can modify the list.'''

# def local_extrema(A):
# 	count = 0
# 	if len(A) <= 2:
# 		return len(A)

# 	new_A = []
# 	for i in xrange(0, len(A)):   #remove the adjacent duplicated element
# 		new_A.append(A[i])
# 		if A[i] == A[i-1]:
# 			new_A.pop()
# 	print new_A

# 	for i in xrange(1, len(new_A)-1):
# 		if (new_A[i] < new_A[i-1] and new_A[i] < new_A[i+1]):	#local min
# 			count += 1
# 		if (new_A[i] > new_A[i-1] and new_A[i] > new_A[i+1]):	#local max
# 			count += 1
# 	return count+2

# A = [2,2,3,4,3,3,2,2,1,1,2,5]
# print local_extrema(A)

# '''Google online Coding Assessment:
# return the maximum sum of any non-negative slices of a list
# return -1 if there is no non-negative slices
# worst case time camplexity is expected to be O(N)
# can modify the list.'''

# def non_negative(A):
# 	maximum_final = 0
# 	i = 0
# 	maximum = 0

# 	negative = True			#check wether it is all negative
# 	for x in xrange(1,10):
# 		if x >= 0:
# 			negative = False
# 	if negative:
# 		return -1

# 	while(i < len(A)):
# 		if A[i] >= 0:
# 			maximum += A[i]
# 			i += 1
# 		else:
# 			maximum = 0
# 			i += 1
# 		if maximum > maximum_final:
# 			maximum_final = maximum
# 	return maximum_final

# A = [1,2,-3,4,5,6,-6,14]
# print non_negative(A)


# '''Google Online Coding Assessment:
# Find the equilibrium point of a list
# eg. for [-1,3,-4,5,1,-6,2,1] return [1,3,7] 
# because 1: A[0] = -1 = A[2] + A[3] + A[4] + A[5] + A[6] + A[7]
# 		3: A[0] + A[1] + A[2] = -2 = A[4] + A[5] + A[6] + A[7]
# 		7: A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = 0
# (Note: sum of zero elemnet is equal to zero, this happends when P=0 or P=N-1)
# worst case time camplexity is expected to be O(N)
# return if no equilibrium found
# can modify the list.'''

# def find_equilibrium(A):
# 	possible_output = {0:0}
# 	solution_list = []
# 	sum = 0
# 	for each in A:
# 		sum += each

# 	sum_left = 0
# 	for i in xrange(1,len(A)):
# 		sum_left += A[i-1]
# 		possible_output[i] = sum_left
# 	print possible_output

# 	for a, b in possible_output.items():
# 		if (b == sum - b - A[a]):
# 			solution_list.append(a)

# 	if solution_list:
# 		return solution_list
# 	else:
# 		return -1

# A = [-1,3,-4,5,1,-6,2,1]
# B = [-7,1,5,2,-4,3,0]
# C = [0,0,0,0,0,0]
# D = [1,2,4]
# print find_equilibrium(D)

# Combination Sum 
# class Solution:
#     # @param candidates, a list of integers
#     # @param target, integer
#     # @return a list of lists of integers
#     def combinationSum(self, candidates, target):
#         candidates.sort()
#         self.solution_list = []
#         new_list = []
#         self.DFS(candidates, target, new_list)
#         return self.solution_list

#     def DFS(self, candidates, target, new_list):
#         if target == 0:
#             new_list.sort()
#             if not(new_list in self.solution_list):
#                 v_list = new_list[:]
#                 # self.solution_list += [v_list]
#                 self.solution_list.append(v_list)

#         for i in xrange(0, len(candidates)):
#             if target < candidates[i]:
#                 return 
#             target -= candidates[i]
#             # new_list.append(candidates[i])
#             self.DFS(candidates, target, new_list + [candidates[i]])
#             target += candidates[i]
#             # new_list.pop()

# s = Solution()
# # A = [2,3,6,7]
# A = [8,7,4,3]
# # A = [7]
# print s.combinationSum(A, 11)

# # Combinations
# class Solution:
#     # @return a list of lists of integers
#     def combine(self, n, k):
#         self.solution_list = []
#         new_list = []
#         data_list = []
#         for i in xrange(1, n + 1):
#             data_list.append(i)
#         self.DFS(data_list, n, k, 0, new_list)
#         return self.solution_list

#     def DFS(self, data_list, n, k, start, new_list):
#         if k == 0:
#             self.solution_list.append(new_list)
#             return

#         for i in xrange(start, n):
#             self.DFS(data_list, n, k - 1, i + 1, new_list + [data_list[i]])
#         return self.solution_list


# s = Solution()
# print s.combine(1,0)

# Combination Sum 
# class Solution:
#     # @param candidates, a list of integers
#     # @param target, integer
#     # @return a list of lists of integers
#     def combinationSum(self, candidates, target):
#         candidates.sort()
#         self.solution_list = []
#         new_list = []
#         self.DFS(candidates, target, new_list)
#         return self.solution_list
        
#     def DFS(self, candidates, target, new_list):
#         if target < 0:
#             return
#         if target == 0:
#             new_list.sort()
#             if not(new_list in self.solution_list):
#                 self.solution_list.append(new_list)
#             return 
#         for i in xrange(0, len(candidates)):
#             if target < candidates[i]:
#                 break
#             self.DFS(candidates, target - candidates[i], new_list + [candidates[i]])

# s = Solution()
# A = [3, 5, 4, 6, 9]
# print s.combinationSum(A, 15)



