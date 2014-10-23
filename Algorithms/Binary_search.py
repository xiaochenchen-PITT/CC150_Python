# Key point of Binary search: list does not need to be sliced. just
# pass the imin and imax!
# And list has to be sorted!
def BinarySearch_Recur(lst, target, imin, imax):
	if len(lst) == 0:
		return -1
	if imin > imax:
		return -1		# No key found
	imid = imin + (imax - imin) / 2
	if target < lst[imid]:
		return BinarySearch_Recur(lst, target, imin, imid - 1)
	elif target > lst[imid]:
		return BinarySearch_Recur(lst, target, imid + 1, imax)
	else:
		return imid

def BinarySearch_Iter(lst, target, imin, imax):
	if len(lst) == 0:
		return -1
	while imin <= imax:
		imid = imin + (imax - imin) / 2
		if target < lst[imid]:
			imax = imid - 1
		elif target > lst[imid]:
			imin = imid + 1
		else:
			return imid
	return -1    # No key found


A = [1,2,3,4,5,6]
# A = []
print BinarySearch_Recur(A, 3, 0, 5)
print BinarySearch_Iter(A, 6, 0, 5)