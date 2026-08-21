class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        seen = set()

        left,right = 0,0
        # seen.add(s[left])
        
        while right < len(s):
                if s[right] not in seen:
                        seen.add(s[right])
                        right +=1
                else:
                        while s[right] in seen:
                                seen.remove(s[left])
                                left+=1
                maxl = max(maxl, right-left)

        return maxl