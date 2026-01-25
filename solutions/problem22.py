class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.combinations = []
        self.hash_combination = {}
        self.n = n

    def backtrack(self, combination):
        if len(combination) == 2*self.n:
            self.combinations.append(combination)
        
        for input_place in range()