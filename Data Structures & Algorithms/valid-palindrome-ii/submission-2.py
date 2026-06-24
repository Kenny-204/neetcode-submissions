class Solution:
    def validPalindrome(self, s: str) -> bool:
        def plain(s):
            left = 0
            right = len(s) -1

            while left < right:
                if s[left] == s[right]:
                    left+=1
                    right -=1
                else:
                    return False
            return True
        
        left = 0
        right = len(s) -1
# abbda
        while left < right:
            if s[left] != s[right]:

                if plain(s[left+1:right+1]) or plain(s[left:right]):
                    return True
                else: return False
            else:
                left+=1
                right -=1
        return True
