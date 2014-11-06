class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        if numRows == 0:
            return res
        for i in range(1, numRows+1):
            arr = [1]
            start = 0
            while len(arr) < i:
                num = (res[i-2][start]+res[i-2][start+1]) if start < i - 2 else 1 
                arr.append(num)
                start += 1
            res.append(arr)
        return res