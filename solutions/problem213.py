class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        nums_1 = nums[0:-1]
        nums_2 = nums[1:]
        dp_1 = [0 for _ in range(len(nums_1))]
        dp_2 = [0 for _ in range(len(nums_2))]
        dp_1[0] = nums_1[0]
        dp_1[1] = max(nums_1[1], nums_1[0])
        dp_2[0] = nums_2[0]
        dp_2[1] = max(nums_2[1], nums_2[0])
        for i in range(2, len(nums_1)):
            dp_1[i] = max(dp_1[i - 2] + nums_1[i], dp_1[i - 1])
            dp_2[i] = max(dp_2[i - 2] + nums_2[i], dp_2[i - 1])
        return max(dp_1[-1], dp_2[-1])

s = Solution()
print(s.rob([1,2,1,1]))