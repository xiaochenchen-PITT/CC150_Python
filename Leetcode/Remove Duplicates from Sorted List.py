# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        '''hint: pay attention to all None cases!!!'''
        currnode = head
        while currnode and currnode.next:
            while currnode.next:
                if currnode.val == currnode.next.val:
                    currnode.next = currnode.next.next
                else:
                    break
            currnode = currnode.next
        return head