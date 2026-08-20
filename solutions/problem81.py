class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if nums is None:
            return False
        if len(nums) == 1:
            return target in nums
        if len(nums) == 0:
            return False
        l, r = 0, len(nums) - 1
        self.nums = nums
        self.target = target
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[m] > nums[r]:
                if self.binary_search(l, m):
                    return True
                l = m + 1
            elif nums[m] < nums[r]:
                if self.binary_search(m, r):
                    return True
                r = m - 1
            else:
                r -= 1
        return False

    def binary_search(self, l, r):
        while l <= r:
            m = (l + r) // 2
            if self.nums[m] == self.target:
                return True
            elif self.nums[m] < self.target:
                l = m + 1
            else:
                r = m - 1
        return False

#[4,5,6,6,7,0,1,2,4,4] len = 10
s = Solution()
s.search(nums = [1,0,1,1,1], target = 0)
# print(s.search(nums = [2,5,6,0,0,1,2], target = 3))
# print(s.search(nums = [1,2,2,2,2], target = 2))