#2,34% speed beaten
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.combinations = []
        self.short_combinations = []
        self.nums = nums
        self.backtrack(combination=[])
        return self.combinations

    def backtrack(self, combination):
        if len(combination) == len(self.nums):
            if combination not in self.combinations:
                self.combinations.append(combination[:])
        
        for var in self.nums:
            if var in combination:
                continue
            combination.append(var)
            self.backtrack(combination)
            combination.pop()

#11.64% speed beaten
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.combinations = []
        self.short_combinations = []
        self.nums = nums
        self.backtrack(combination=[])
        return self.combinations

    def backtrack(self, combination):
        if len(combination) == len(self.nums):
            self.combinations.append(combination[:])
        
        for var in self.nums:
            if var in combination:
                continue
            combination.append(var)
            self.backtrack(combination)
            combination.pop()

s = Solution()
print(s.permute([1,2,3]))