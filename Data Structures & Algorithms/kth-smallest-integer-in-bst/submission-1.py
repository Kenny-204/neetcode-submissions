# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        stack = []
        curr = root
        while curr or stack:
            # go to the leftest end
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            # process current
            res += 1
            if res == k:
                return curr.val

            # go right
            curr = curr.right

                    