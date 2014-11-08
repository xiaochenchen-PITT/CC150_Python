# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        dummynode = ListNode(32)
        dummynode.next = head
        currnode = head
        count = 1 # how many nodes are there except the dummy node
        while currnode.next:
            currnode = currnode.next
            count += 1
        currnode = dummynode
        i = 0
        while i != count-n:
            currnode = currnode.next
            i += 1
        currnode.next = currnode.next.next # skip the node
        return dummynode.next