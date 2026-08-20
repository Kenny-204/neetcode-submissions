class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close = {"}":"{","]":"[",")":"("}

        for i in range(len(s)):
            if s[i] not in close:
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                curr = stack.pop()
                if curr != close[s[i]]:
                    return False
        if stack != []:
            return False
        else : return True 