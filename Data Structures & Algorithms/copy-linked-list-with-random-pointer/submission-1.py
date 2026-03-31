"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        hashmap = {}
        new_head = Node(head.val)
        curr = new_head
        curr_head = head

        while curr:
            hashmap[curr_head] = curr
            if curr_head.next:
                curr.next = Node(curr_head.next.val) or None
            else:
                curr.next = None
            # curr.random = None
            curr = curr.next
            curr_head = curr_head.next

        curr = new_head
        curr_head = head
        # print(hashmap)
        while curr:
            if curr_head.random is not None:
                curr.random = hashmap[curr_head.random]
            else:
                curr.random = None
            curr = curr.next
            curr_head = curr_head.next
        return new_head
