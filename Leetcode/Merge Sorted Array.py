class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
	def merge(self, A, m, B, n):
		'''Note: A is actually [1, 3, 6, placeholder, placeholder], m = 3
				B is [2, 5], n = 2
				So avoid using len(A) and len(B), use m and n with incre/decre.
				And avoid using append() and extend()'''
		if n == 0:
			return
			
		pa = 0
		pb = 0
		while n - pb > 0:
			if pa > m-1:
				for i in range(pb, n):
				    A[pa] = B[i]
				    pa += 1
				m += n
				break
			if B[pb] >= A[pa]:
				pa += 1
			else:
				A.insert(pa, B[pb])
				pb += 1
				m += 1
		return