class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right = 0, 1
        maxcount = 0

        for right in range(len(s)):
                while s[right] in seen:
                        seen.remove(s[left])
                        left += 1
                seen.add(s[right])
                maxcount = max(maxcount, right - left +1)
        return maxcount
