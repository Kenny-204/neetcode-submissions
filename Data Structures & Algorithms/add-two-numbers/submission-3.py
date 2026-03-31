# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        res = ListNode(0)
        curr1 = l1
        curr2 = l2
        curr3 = res
        while curr1 and curr2:
            sum = curr1.val + curr2.val + remainder
            if remainder > 0:
                remainder = 0
            if sum >= 10:
                digits = str(sum)
                digit1, digit2 = int(digits[0]), int(digits[1])
                print(digit1, digit2)
                curr3.next = ListNode(digit2)
                remainder = digit1
            else:
                curr3.next = ListNode(sum)
            curr1 = curr1.next
            curr2 = curr2.next
            curr3 = curr3.next
        while curr1:
            sum = curr1.val  + remainder
            if remainder > 0:
                remainder = 0
            if sum >= 10:
                digits = str(sum)
                digit1, digit2 = int(digits[0]), int(digits[1])
                curr3.next = ListNode(digit2)
                remainder = digit1
            else:
                curr3.next = ListNode(sum)
            curr3 = curr3.next
            curr1 = curr1.next
        while curr2:
            sum = curr2.val + remainder
            if remainder > 0:
                remainder = 0
            if sum >= 10:
                digits = str(sum)
                digit1, digit2 = int(digits[0]), int(digits[1])
                curr3.next = ListNode(digit2)
                remainder = digit1
            else:
                curr3.next = ListNode(sum)
            curr3 = curr3.next
            curr2 = curr2.next
        if remainder > 0:
            curr3.next = ListNode(remainder)

        return res.next