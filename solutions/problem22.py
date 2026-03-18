class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.combinations = set()
        self.n = n
        self.backtrack([], 0, 0)
        return list(self.combinations)
    
    def backtrack(self, combination, amount_of_left_brackets, amount_of_right_brackets):
        if self.n == amount_of_left_brackets == amount_of_right_brackets:
            self.combinations.add("".join(combination))
            return
        
        for var in ("(", ")"):
            if var == "(":
                amount_of_left_brackets += 1
            else:
                amount_of_right_brackets += 1
            if amount_of_left_brackets < amount_of_right_brackets:
                amount_of_right_brackets -= 1
                continue
            if amount_of_left_brackets > self.n:
                amount_of_left_brackets -= 1
                continue
            combination.append(var)
            self.backtrack(combination, amount_of_left_brackets, amount_of_right_brackets)
            combination.pop()
            if var == "(":
                amount_of_left_brackets -= 1
            else:
                amount_of_right_brackets -= 1

s = Solution()
print(s.generateParenthesis(3))