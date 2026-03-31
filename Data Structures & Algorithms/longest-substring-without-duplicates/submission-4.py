class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxcount = 0
        left, right = 0, 1

        if s == "":
                return 0
        if len(s) == 1:
                return 1

        currentcount = 0
        while right < len(s):
                if left == 0 and right == 1:
                        if s[left] != s[right]:
                                seen[s[left]] = True
                                seen[s[right]] = True
                                currentcount = 2
                                right += 1
                                maxcount = max(maxcount, currentcount)

                        else:
                                seen[s[left]] = True
                                currentcount = 1
                                left = right
                                right += 1
                                maxcount = max(maxcount, currentcount)
                else:
                        if seen.get(s[right]) == True:
                                maxcount = max(maxcount, currentcount)
                                seen[s[left]] = False
                                left += 1
                                currentcount -= 1
                        else:
                                currentcount += 1
                                maxcount = max(maxcount, currentcount)
                                seen[s[right]] = True
                                right += 1
        return maxcount   