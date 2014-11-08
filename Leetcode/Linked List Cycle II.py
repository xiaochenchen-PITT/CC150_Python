# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node

    # def detectCycle(self, head):
    #     # using extra space
    #     visited = [head]
    #     faster = head
    #     slower= head
    #     while faster and faster.next:
    #         faster = faster.next.next
    #         slower = slower.next
            
    #         if slower not in visited:
    #             visited.append(slower)
    #         if faster in visited:
    #             n = visited.index(faster)

    #         if faster == slower:
    #             return visited[n-1]
    #     return 

    def detectCycle(self, head):
        # not using extra space
        # famous cycle detection algorithm - Floyd's cycle detection algorithm, aka hare-tortoise algorithm.
        faster = head
        slower= head
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                p1 = head
                p2 = faster # current position
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return 
