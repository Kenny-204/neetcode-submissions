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
        visited = {}
        curr = root
        while curr or stack:
            stack.append(curr)
            if curr.left and curr.left not in visited:
                curr = curr.left
            else:
                res += 1
                processing = stack.pop()
                if res == k:
                    return processing.val
                visited[processing] = True
                if processing.right:
                    curr = processing.right
                else:
                    if stack:
                        curr = stack.pop()
                    else:
                        break
                