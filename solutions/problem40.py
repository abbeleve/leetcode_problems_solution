class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.combinations = []
        self.candidates = candidates
        self.target = target
        if sum(candidates) < target:
            return []
        candidates.sort()
        self.backtrack([], -1)

        return self.combinations

    def backtrack(self, combination, index):
        if sum(combination) > self.target:
            return
        if sum(combination) == self.target:
            combination = combination[:]
            self.combinations.append(combination)
            return
        
        for candidate_index in range(index + 1, len(self.candidates)):
            candidate = self.candidates[candidate_index]
            if candidate_index > index + 1 and candidate == self.candidates[candidate_index - 1]:
                continue
            if sum(combination) + candidate > self.target:
                break
            combination.append(candidate)
            self.backtrack(combination, candidate_index)
            combination.pop()

s = Solution()
print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
        
