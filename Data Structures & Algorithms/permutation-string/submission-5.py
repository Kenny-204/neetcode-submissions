class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        count = {}
        s1count = {}
        if len(s2) < len(s1): return False

        for letter in s1:
            if letter in s1count:
                s1count[letter] += 1
            else:
                s1count[letter] = 1

        while right <= len(s2):
            while right - left < len(s1):
                if s2[right] in count:
                    count[s2[right]] += 1
                else:
                    count[s2[right]] = 1
                right += 1
            if count == s1count:
                return True
            else:
                if count[s2[left]] > 1:
                    count[s2[left]] -= 1
                else:
                    del count[s2[left]]
                left += 1
                if right < len(s2):
                    if s2[right] in count:
                        count[s2[right]] += 1
                    else:
                        count[s2[right]] = 1
                right += 1
        return False
