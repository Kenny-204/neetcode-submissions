# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}

        if not head:
            return False

        node = head

        while node:
            if node in seen:
                return True
            else:
                seen[node] = True
                node = node.next
        return False