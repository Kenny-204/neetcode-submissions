class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        combination = []

        def dfs(i):
            if len(combination) == k:
                res.append(combination.copy())
                return
            
            if i > n :
                return

            combination.append(i)
            dfs(i+1)
            combination.pop()
            dfs(i+1)

        dfs(1)
        return res