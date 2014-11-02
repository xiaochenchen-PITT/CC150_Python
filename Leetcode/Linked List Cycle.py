# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    # using extra space
        # current_node = head
        # visited = []
        # while current_node:
        # 	if current_node not in visited:
        # 		visited.append(current_node)
        # 	else:
        # 		return False
        # 	current_node = current_node.next
        # return True

        # Not using extra space
        # two pointers
	    if not head:
	    	return False
	    faster = head
	    slower = head.next
	    while faster and slower:
	    	if faster.val == slower.val:
	     		return True
	     	faster = faster.next.next
	     	slower = slower.next
	    return False
