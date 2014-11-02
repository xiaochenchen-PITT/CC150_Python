'''5.1 You are given two 32-bit numbers, N and M, and two bit positions, 
i and j Write a method to set all bits between i and j in N equal to M 
(e g , M becomes a substring of N located at i and starting at j)
EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
'''
# def SetBit(N, M, i, j):
# 	'''Assume N is larger than M and j is larger than i.'''
# 	if 2**(j-i+1) < M:
# 		raise ValueError('Invalid i and j!')
# 	all1s = 0xffffffff
# 	mask = all1s - ((1<<j+1)-1) + ((1<<i)-1)
# 	print bin(mask)
# 	N1 = mask & N
# 	M1 = (0x00000000 | M) << i
# 	return bin(N1 | M1)

# print SetBit(0b10000000000, 0b10101, 2, 6)

'''5.2 Given a (decimal - e.g 3.72) number that is passed in as a string, 
print the binary representation. If the number can not be represented 
accurately in binary, print "ERROR".
'''
# def BinRepr(string):
# 	lst = string.split('.')
# 	n = lst[0] # string
# 	deci = '0.'+lst[1] # string
# 	# print n, deci
# 	int_str = ''
# 	deci_str = ''

# 	# integer
# 	n = int(n)
# 	while n != 0:
# 		mod = n % 2
# 		int_str += str(mod)
# 		n = n / 2
# 	# print int_str

# 	# decimal
# 	n = float(deci)
# 	while True: # decimal part may run forever
# 		n = n * 2
# 		if n > 1:
# 			deci_str += '1'
# 			n = n - 1
# 		elif n < 1:
# 			deci_str += '0'
# 		else:
# 			deci_str += '1'
# 			break
# 		if len(deci_str) > 32:
# 			return "ERROR"
# 	# print deci_str
# 	return int_str + '.' + deci_str

# print BinRepr('3.25')
# print BinRepr('13.325')

'''5.3 Given an integer, print the next larger number that 
have the same number of 1 bits in their binary representation.
'''
# def FindNextLarger(n):
# 	if n == 0:
# 		return 0
# 	# count how many 1's in the number
# 	n_str = bin(n)
# 	count_n = 0
# 	for x in n_str:
# 		if x == '1':
# 			count_n += 1
# 	# increase 1 at a time, stops when count = count_n
# 	count = 0
# 	while count != count_n:
# 		n += 1
# 		n_str = bin(n)
# 		count = 0
# 		for x in n_str:
# 			if x == '1':
# 				count += 1
# 	return n

# print FindNextLarger(13)

'''5.4 Explain what the following code does: (n & (n-1)) == 0
Answer: 1000000 & 0111111 = 0 -> checks wether n is a power of 2.
'''

'''5.5 Write a function to determine the number of bits required to convert 
integer A to integer B
Input: 31, 14 Output: 2
'''
# def BitsSwapReq(a, b):
# 	c = bin(a ^ b)
# 	count = 0
# 	for x in c:
# 		if x == '1':
# 			count += 1
# 	return count 

# print BitsSwapReq(31, 14)

'''5.6 Write a program to swap odd and even bits in an integer with 
as few instructions as possible (eg, bit 0 and bit 1 are swapped, 
bit 2 and bit 3 are swapped, etc)
'''
# def SwapOddEvenBits(n):
# 	'''Assume the number is just 4 bits'''
# 	Odd_shift = n & 0b1010
# 	Even_shift = n & 0b0101
# 	return bin((Odd_shift >> 1) | (Even_shift << 1))
# print SwapOddEvenBits(11)



