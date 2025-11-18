class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        max_num_occasions = 0
        for num in unique_nums:
            num_occasions = nums.count(num)
            if num_occasions > max_num_occasions:
                res = num
                max_num_occasions = num_occasions
        return res

    
s = Solution()
print(s.majorityElement([3,3,4]))