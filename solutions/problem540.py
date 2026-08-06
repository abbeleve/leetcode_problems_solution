class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if nums is None:
            return None
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == nums[m - 1]:
                if m % 2 == 0:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] == nums[m + 1]:
                if m % 2 == 0:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return nums[m]
        return nums[l]

s = Solution()
print(s.singleNonDuplicate(nums = [3,3,7,7,10,11,11]))