from copy import deepcopy

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        suffix = deepcopy(nums)
        for i in range(len(nums) - 1, 0, -1):
            if i != len(nums) - 1:
                suffix[i] = suffix[i + 1] * nums[i]
        
        prefix = deepcopy(nums)
        for i in range(len(nums)):
            if i != 0:
                prefix[i] = prefix[i - 1] * nums[i]
        print(suffix)
        print(prefix)

        result = []
        for index, num in enumerate(nums):
            if index == 0:
                result.append(suffix[index + 1])
                continue
            if index == len(nums) - 1:
                result.append(prefix[index - 1])
                continue
            result.append(prefix[index - 1] * suffix[index + 1])
        return result
                
s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))