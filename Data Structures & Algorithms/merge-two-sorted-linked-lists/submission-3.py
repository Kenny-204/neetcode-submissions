# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        nodel = dummy
        nodel1 = list1
        nodel2 = list2
        while nodel1 and nodel2 :
            if nodel1.val <nodel2.val:
                
                nodel.next = nodel1
                nodel = nodel.next
                nodel1 = nodel1.next
                
            else:
                nodel.next = nodel2
                nodel = nodel.next
                nodel2 = nodel2.next
            
            
        if nodel1:
            nodel.next = nodel1
        else:
            nodel.next = nodel2
        
        return dummy.next