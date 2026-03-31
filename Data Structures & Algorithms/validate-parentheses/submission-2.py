class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {"}": "{", "]": "[", ")": "("}
        if len(s) == 1:
            return False
        for bracket in s:
            if bracket in close:
                if len(stack) == 0:
                    return False
                if stack[-1] != close[bracket]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(bracket)

        if len(stack) != 0:
            return False

        else:
            return True