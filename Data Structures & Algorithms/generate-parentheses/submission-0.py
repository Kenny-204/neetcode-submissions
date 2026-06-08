class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        curr = []

        def dfs(openno, close):
            if openno == close == n:
                res.append("".join(curr.copy()))
                return


            if openno < n:
                curr.append("(")
                dfs(openno + 1, close)
                curr.pop()

            if close < openno and close < n:
                curr.append(")")
                dfs(openno, close + 1)
                curr.pop()


        dfs(0, 0)
        return res
