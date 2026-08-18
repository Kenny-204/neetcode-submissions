class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for st in s:
            if st in map1:
                map1[st] = map1[st] +1
            else:map1[st] = 1
        for ts in t:
            if ts in map2:
                map2[ts] = map2[ts] +1
            else:map2[ts] = 1
        
        return map1 == map2