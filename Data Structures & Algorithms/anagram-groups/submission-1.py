class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for st in strs:
            sort = "".join(sorted(st))
            if sort in map:
                 map[sort].append(st)
            else:
                map[sort] = [st]
        return list(map.values())