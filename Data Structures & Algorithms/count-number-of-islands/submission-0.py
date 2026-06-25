class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        path = set()

        def dfs(r, c):

            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in path:
                return
            if grid[r][c] == "0":
                return
            path.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in path:
                    islands += 1
                    dfs(r, c)
        return islands