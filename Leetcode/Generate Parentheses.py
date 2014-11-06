class Solution:
    # @param an integer
    # @return a list of string
    def isValid(self, s):
    	# checking if a string is a pair of well-formed parentheses.
		left_count = 0
		right_count = 0
		for c in s:
			if c == '(':
				left_count += 1
			else:
				right_count += 1
			if right_count > left_count:
				return False
		return True

    def DFS(self, n, s, left, right):
    	if left + right == 2*n:
    		if left == right:
    			if self.isValid(s):
    				self.res.append(s)
    		return
    	for next in ['(', ')']:
    		if next == '(':
    			self.DFS(n, s + next, left + 1, right)
    		else:
	    		self.DFS(n, s + next, left, right + 1)

    def generateParenthesis(self, n):
    	'''hint: beginning is "(", then DFS adding "(" or ")".'''
    	self.res = []
    	self.DFS(n, '(', 1, 0)
    	return self.res

s = Solution()
print s.generateParenthesis(4)
