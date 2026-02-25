class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.combinations = []
        self.nums = nums
        self.process([], 0)
        return self.combinations

    def process(self, combination, index):
        comb = sorted(combination)
        if comb not in self.combinations:
            self.combinations.append(comb)
        else:
            return
        
        for i in range(index, len(self.nums)):
            subset = self.nums[i]
            combination.append(subset)
            self.process(combination, i + 1)
            combination.pop()

s = Solution()
print(s.subsetsWithDup([4,1,0]))
