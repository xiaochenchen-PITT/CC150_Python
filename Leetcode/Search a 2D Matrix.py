class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    flag = False
    def searchMatrix(self, matrix, target):
		if len(matrix) > 1:
			mid = (len(matrix)-1) / 2
			# print mid
			if matrix[mid][-1] < target:
				sliced_mat = matrix[mid+1:]
			elif matrix[mid][-1] > target:
				sliced_mat = matrix[:mid+1]
			else:
				self.flag = True
				return self.flag # attention: could exit here!
			self.searchMatrix(sliced_mat, target)
		if len(matrix) == 1:
			if len(matrix[0]) == 1 or len(matrix[0]) == 2:
				if target in matrix[0]:
					self.flag = True
				return self.flag
			mid = (len(matrix[0])-1) / 2
			if matrix[0][mid] > target:
				sliced_mat = matrix[0][:mid+1]
			elif matrix[0][mid] < target:
				sliced_mat = matrix[0][mid+1:]
			else: 
				self.flag = True
				return self.flag # attention: could exit here!
			self.searchMatrix([sliced_mat], target)
		return self.flag # overall return
