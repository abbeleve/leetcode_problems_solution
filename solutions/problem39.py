class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.combinations = []
        self.hash_combinations = {}
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.backtrack([], 0)
        return list(set(tuple(inner_list) for inner_list in self.combinations))

    def backtrack(self, combination, sums):
        if sums == self.target:
            combination_ = combination[:]
            combination_.sort()
            if tuple(combination_) in self.hash_combinations:
                return
            
            self.combinations.append(combination_)
            self.hash_combinations[tuple(combination_)] = True
        
        for var in self.candidates:
            if sums + var > self.target:
                return
            combination.append(var)
            sums += var
            self.backtrack(combination, sums)
            combination.pop()
            sums -= var
        
s = Solution()

print(s.combinationSum(candidates = [2,3,6,7], target = 7))