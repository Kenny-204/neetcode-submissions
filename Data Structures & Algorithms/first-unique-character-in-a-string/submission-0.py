class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for st in s:
            if st in count:
                count[st] +=1
            else: count[st] = 1

        for i,st in enumerate(s):
            if count[st] ==1:
                return i
        return -1