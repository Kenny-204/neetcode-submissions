# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      
        def splitList(head):
            slow, fast = head, head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            slow = slow.next
            prev = prev.next
            prev.next = None

            return head, slow


        def reverseList(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev


        def mergeLists(first, second):
            head = first
            while first and second:
                temp1 = head.next
                temp2 = second.next

                head.next = second
                second.next = temp1
                head = temp1
                second = temp2
            
        if not head.next or not head:
            return
            # first divide the list into two halves first half and second half
        first_half_of_list, second_half_of_list = splitList(head)
        # reverse the second half
        reversed_second_half = reverseList(second_half_of_list)
        # merge the two lists into one
        mergeLists(first_half_of_list, reversed_second_half)
