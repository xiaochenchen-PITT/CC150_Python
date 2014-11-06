class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        i = len(digits) - 1  # last element
        self.iteration(digits, i)
        return digits
        
    def iteration(self, digits, i):
        digits[i] += 1
        if digits[i] > 9: 
            if i == 0: # it is the first element
                digits[i] = 0
                digits.insert(0, 1)
            else:
                digits[i] = 0
                self.iteration(digits, i - 1)
        
s = Solution()
A = [5,7,8]
print s.plusOne([5,7,8])
print s.plusOne([5,9,9])
print s.plusOne([9,9])
