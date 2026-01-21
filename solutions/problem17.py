class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.combinations = []
        self.mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.backtrack("", digits)
        return self.combinations

    def backtrack(self, combination, digits):
        if len(combination) == len(digits):
            self.combinations.append(combination)
            return
        for var in self.mapping[digits[len(combination)]]:
            if combination + var not in self.combinations:
                self.backtrack(combination + var, digits)

s = Solution()
print(s.letterCombinations(digits='23'))