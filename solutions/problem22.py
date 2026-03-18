class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.combinations = set()
        self.n = n
        self.backtrack([])
        return list(self.combinations)
    
    def backtrack(self, combination):
        if self.n == combination.count("(") == combination.count(")"):
            self.combinations.add("".join(combination))
            return
        
        for var in ("(", ")"):
            combination.append(var)
            if combination.count("(") < combination.count(")"):
                combination.pop()
                continue
            if combination.count("(") > self.n:
                combination.pop()
                continue
            self.backtrack(combination)
            combination.pop()

s = Solution()
print(s.generateParenthesis(3))