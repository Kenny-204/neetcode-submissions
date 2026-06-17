class Solution:
    def validPalindrome(self,word):
            if(len(word) == 0):
                return False
            if(len(word) == 1):
                return True

            left = 0
            right = len(word) -1
            
            while left< right:
                if word[left] == word[right]:
                    left+=1
                    right-=1
                
                else :return False
            return True
    def partition(self, s: str) -> List[List[str]]:
        res = []

        part = []
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.validPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

                
            