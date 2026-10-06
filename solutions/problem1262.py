class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        res_sum = sum(nums)
        nums = sorted(nums)
        module = [i % 3 for i in nums if i % 3 != 0]
        nums = [i for i in nums if i % 3 != 0]
        sum_module = res_sum % 3
        if sum_module == 0:
            return res_sum
        if sum_module == 1:
            try:
                ones = nums[module.index(1)]
            except:
                ones = float('inf')
            try:
                twos_1 = nums[module.index(2)]
                twos_2 = nums[module.index(2, module.index(2) + 1)]
                twos = twos_1 + twos_2
            except:
                twos = float('inf')
            return max(0, max(res_sum - ones, res_sum - twos))
        if sum_module == 2:
            try:
                twos = nums[module.index(2)]
            except:
                twos = float('inf')
            try:
                ones_1 = nums[module.index(1)]
                ones_2 = nums[module.index(1, module.index(1) + 1)]
                ones = ones_1 + ones_2
            except:
                ones = float('inf')
            return max(0, max(res_sum - ones, res_sum - twos))

s = Solution()
print(s.maxSumDivThree([3,6,5,1,8]))