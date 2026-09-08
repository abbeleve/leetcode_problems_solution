class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        num_patches = 0
        if nums[0] != 1:
            nums.insert(0, 1)
            num_patches += 1
        i = 0
        while i < len(nums):
            if nums[i] < n:
                i += 1
            else:
                break
        nums.insert(i, n)
        nums = nums[0:i + 1]
        prefix_sum = 0
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if i == len(nums) - 2:
                if prefix_sum >= nums[i + 1]:
                    continue
                while prefix_sum < nums[i + 1]:
                    new_patch = prefix_sum + 1
                    prefix_sum += new_patch
                    num_patches += 1
            if prefix_sum >= nums[i + 1] - 1:
                continue
            while prefix_sum < nums[i + 1] - 1:
                new_patch = prefix_sum + 1
                prefix_sum += new_patch
                num_patches += 1
        return num_patches

s = Solution()
print(s.minPatches(nums = [1,12,15], n = 43))