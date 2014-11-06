# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
    	if not head or not head.next:
    		return head

    	dummnode = ListNode(32)
    	currnode = dummnode
    	dummnode.next = head
    	while currnode.next and currnode.next.next:
    		currnode.next = self.swap(currnode.next, currnode.next.next)
    		currnode = currnode.next.next
    	return dummnode.next

    def swap(self, n1, n2):
    	t = n2.next
    	n2.next = n1
    	n1.next = t
    	return n2
    	
