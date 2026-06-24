# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        def postorder(root):
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            if root.val >=low and root.val <= high:
                self.res += root.val
        postorder(root)
        return self.res