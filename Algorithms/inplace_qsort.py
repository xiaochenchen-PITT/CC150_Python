# def partition(lst, left, right):
#     pivot = left
#     left_index = left+1
#     right_index = right

#     while left_index <= right_index:
#         while lst[left_index] < lst[pivot]:
#             left_index += 1
#         while lst[right_index] > lst[pivot]:
#             right_index -= 1
#         if right_index <= left_index:
#             lst[right_index], lst[pivot] = lst[pivot], lst[right_index]
#             return right_index
#         else:
#             lst[right_index], lst[left_index] = lst[left_index], lst[right_index]
#             left_index += 1
#             right_index -= 1

#     lst[right_index], lst[pivot] = lst[pivot], lst[right_index]
#     return right_index

def partition(a, left, right):
    pivot = a[right]
    for i in xrange(left, right):
        if a[i] < pivot:
            a[left], a[i] = a[i], a[left]
            left += 1
    a[right], a[left] = a[left], a[right]
    return left

def inplace_qsort(a, left, right):
    if left < right:
        new_pivot = partition(a,left,right)
        inplace_qsort(a, left, new_pivot-1)
        inplace_qsort(a, new_pivot+1, right)
        return a

A = [5,8,64,32,100,65,39,45]
print inplace_qsort(A, 0, len(A)-1)


# # Appendix:
# # Quick sort (NO in place)
# # Quick Sort
# def qsort(lst):
#   if len(lst) <= 1:
#       return lst
#   else:
#       pivot = lst[0]
#       less = []       # what if you can not use additional
#       equal = []      # data structure?  -- In place quick sort
#       greater = []

#       for each in lst:
#           if each < pivot:
#               less.append(each)
#           elif each == pivot:
#               equal.append(each)
#           else:
#               greater.append(each)
#       return qsort(less) + equal + qsort(greater)
