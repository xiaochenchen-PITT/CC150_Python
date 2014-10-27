'''1.Hailstone Value:
if n is odd, n = n * 3 + 1, if n is even, n = n / 2; the number of steps to become
one is defined as Hailstone Value.
'''
# def Find_hailstone_value(n):
# 	if n < 1:
# 		raise ValueError ('n is not a valid number in this question!')
# 	hsv = 0
# 	while n != 1:
# 		if n % 2 == 1: # odd
# 			n = n * 3 + 1
# 		else: # even
# 			n = n / 2
# 		hsv += 1
# 	return hsv

# print Find_hailstone_value(3)

'''2. given n, print all number among (0 , n) whose Hailstone Value is greater than 
that for any previous (smaller) number.'''
# def Print_Hailstone_Value(n):
# 	max_hsv = 0
# 	print max_hsv
# 	for x in xrange(1, n+1):
# 		hsv = Find_hailstone_value(x)
# 		if hsv > max_hsv:
# 			print hsv
# 			max_hsv = hsv

# Print_Hailstone_Value(6)

'''3.How to optimize this function?
'''
# can use DP to optimize, use hash map to keep track the previously computed 
# Hailstone value, so next time you encounter it, don't compute it again, go look 
# for the value in the hash map. ()
import math
def Find_hailstone_value_Opti(n):
	'''Notice that 3-10-5-16-8-4-2-1, if the n is 2 to the n. then just log2n'''
	n_list = []
	hsv_list = []
	mapp = {}
	hsv = 0
	if n < 1:
		raise ValueError ('n is not a valid number in this question!')

	if n & (n - 1) == 0: # if n is pow of 2
		print 'short-cut!'
		return int((math.log(n) / math.log(2)))
	while n != 1:
		n_list.append(n)
		if n % 2 == 1: # odd
			n = n * 3 + 1
		else: # even
			n = n / 2
		hsv += 1
		hsv_list.append(hsv)
	for n in n_list:
		mapp[n] = hsv_list.pop() # this is hash map is useful in Q2
	return hsv

print Find_hailstone_value_Opti(7)



