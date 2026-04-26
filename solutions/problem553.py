class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        obs = "("
        for i in range(1, len(nums)):
            if i == len(nums) - 1:
                obs += str(nums[i]) + ')'
                continue
            obs += str(nums[i]) + '/'
        return str(nums[0]) + "/" + obs