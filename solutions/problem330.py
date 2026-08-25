import math

class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        if nums[0] != 1:
            nums.insert(0, 1)
        num_patches = 0
        diff = 0
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i - 1] + nums[i])
        for i in range(len(sums) - 1):
            prefix_sum = sums[i] + diff
            if prefix_sum >= nums[i + 1] - 1:
                continue
            diff = nums[i + 1] - 1 - prefix_sum
            save_diff = diff
            while save_diff > 0:
                save_diff -= prefix_sum + 1
                num_patches += 1
        print(diff)
        return num_patches
    
s = Solution()
print(s.minPatches(nums = [1,12,15], n = 43))