class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        unique = dict()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[j] + nums[i] == target:
                    return [i, j]
                
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
