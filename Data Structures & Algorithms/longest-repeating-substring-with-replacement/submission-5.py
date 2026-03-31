class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, right = 0, 0
        maxFreq = 0
        res = 0

        while right < len(s):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            maxFreq = max(maxFreq, count[s[right]])

            isValidWindow = ((right - left +1) - maxFreq) <= k
            if isValidWindow:
                right += 1
            else:
                count[s[left]] -= 1
                count[s[right]] -= 1
                left += 1
                maxFreq = max(maxFreq, count[s[right]])
            res = max((right - left ), res)

        return res