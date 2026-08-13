class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        index = len(nums) // 2
        res = 0
        for num in nums:
            res += abs(nums[index] - num)
        return res
        
s = Solution()
print(s.minMoves2(nums = [1,10,2,9]))