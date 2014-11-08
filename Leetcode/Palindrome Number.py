class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        # if extra space is allowed, then it is extremelly simple in Python
        return str(x)[::-1] == str(x)
        
        # hint: use n % 10 to determine if it is palindrome
        if x < 0:
            return False
        reverse = 0
        t = x
        while t:
            mod = t % 10
            reverse = reverse*10 + mod
            t = t /10
        return reverse == x