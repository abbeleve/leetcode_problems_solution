class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        self.valid_combinations = []
        self.k = k
        self.n = n
        self.backtracking([], 0, 1)
        return self.valid_combinations

    def backtracking(self, combination, combination_sum, start):
        if combination_sum == self.n and len(combination) == self.k:
            self.valid_combinations.append(combination[:])
            return
        if len(combination) == self.k:
            return
        
        for number in range(start, 10):
            combination.append(number)
            combination_sum += number
            self.backtracking(combination, combination_sum, number + 1)
            combination.pop()
            combination_sum -= number
        
s = Solution()
print(s.combinationSum3(3, 7))