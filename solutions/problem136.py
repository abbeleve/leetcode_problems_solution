class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        starting_point = 0
        for num in nums:
            starting_point = starting_point ^ num
        return starting_point
    
s = Solution()
print(s.singleNumber([2,2,1]))