# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def deleteNode(head, node):
            curr = head

            prev = curr

            if head == node:
                head = head.next
                node.next = None

            while curr:
                if curr != node:
                    prev = curr
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr.next = None
                    break
            return head
        if not head.next:
            return None
        hashmap = {}
        i = 1

        curr = head
        while curr:
            hashmap[i] = curr
            curr = curr.next
            i += 1
        node_to_delete = i - n 

        head = deleteNode(head, hashmap[node_to_delete])

        return head
