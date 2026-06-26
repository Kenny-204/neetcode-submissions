class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p2 <= len(t):
            if p1 == len(s):
                return True
            if p2 == len(t):
                return False
            if t[p2] == s[p1]:
                p1 += 1
                p2 += 1
            else: 
                p2 += 1
        return False
