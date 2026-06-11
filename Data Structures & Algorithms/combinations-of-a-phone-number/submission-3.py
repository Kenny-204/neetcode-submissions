class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        res = []
        hashmap={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        subset = []
        def backtracking(i):
            if i == len(digits):
                res.append("".join(subset))
                return
            
            for character in hashmap[digits[i]]:
                subset.append(character)
                backtracking(i+1)
                subset.pop()
        backtracking(0)
        return res

