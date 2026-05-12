class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        if target == 0 and nums[0] == 0:
            return 2
        self.combinations = set()
        self.nums = nums
        self.target = target
        self.backtrack([])
        return len(list(self.combinations))

    def backtrack(self, combination):
        if len(combination) == len(self.nums):
            if sum(combination) == self.target:
                self.combinations.add(combination)
            return
            
        for i in range(len(self.nums)):
            if 
            combination.append(self.nums[i])
            self.backtrack(combination)
            combination.pop()
            combination.append((-1) * self.nums[i])
            self.backtrack(combination)
            combination.pop()
        
s = Solution()
print(s.findTargetSumWays([0], 0))