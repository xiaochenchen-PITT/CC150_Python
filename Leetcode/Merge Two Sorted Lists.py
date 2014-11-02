#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode

    # def mergeTwoLists(self, l1, l2):
    #     if not l1 and not l2:
    #         return
    #     if not l2:
    #         return l1
    #     if not l1:
    #         return l2

    #     head = l1 if l1.val < l2.val else l2
    #     if head == l1:
    #         l1 = l1.next
    #     else:
    #         l2 = l2.next
    #     currnode = head
    #     while l1 or l2:
    #         if l1 and l2:
    #             if l1.val < l2.val:
    #                 currnode.next = l1
    #                 l1 = l1.next
    #             else:
    #                 currnode.next = l2
    #                 l2 = l2.next
    #         elif l1:
    #             currnode.next = l1
    #             l1 = l1.next
    #         else:
    #             currnode.next = l2
    #             l2 = l2.next
    #         currnode = currnode.next
    #     return head

    def mergeTwoLists2(self, l1, l2):
        '''Used Dummy node'''
        dummnode = ListNode(32)  # 32 stands for "dummy"
        currnode = dummnode
        while l1 and l2:
            if l1.val < l2.val:
                currnode.next = l1
                l1 = l1.next
            else:
                currnode.next = l2
                l2 = l2.next
            currnode = currnode.next
        currnode.next = l1 and l1 or l2
        return dummnode.next
            