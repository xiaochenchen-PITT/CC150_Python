class Solution:
# @param num, a list of integer
# @return an integer
    def longestConsecutive(self, num):
        '''hint: O(N) means each node can be visited only once. we can set visited list as we scan'''
        maxleng = 0
        visited = []
        for i in range(0, len(num)):
            if num[i] in visited:
                continue
            leng = 1
            visited.append(num[i])
            index = num[i]
            while index + 1 in num:
                leng += 1
                index += 1
                visited.append(index)
            index = num[i]
            while index - 1 in num:
                leng += 1
                index -= 1
                visited.append(index)
            if leng > maxleng:
                maxleng = leng
        return maxleng

s = Solution()
n = [100, 4, 200, 2, 1, 3, 5]
d = {1:1, 2:2}
# print s.longestConsecutive(n)
del n[1]
print d
del d[1]
print d
print n