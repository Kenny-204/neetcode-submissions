# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        # seen = {}

        # if not head:
        #     return False

        # node = head

        # while node:
        #     if node in seen:
        #         return True
        #     else:
        #         seen[node] = True
        #         node = node.next
        # return False