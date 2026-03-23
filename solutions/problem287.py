class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            count = sum(1 for num in nums if num <= mid)
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return int(left)

s = Solution()
print(s.findDuplicate(nums = [1,3,4,2,2,2]))