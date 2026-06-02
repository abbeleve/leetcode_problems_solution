class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        l, r = 0, 1
        result = 0
        if nums is None:
            return 0
        if len(nums) == 1:
            return 1
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                r += 1
            else:
                length = r - l
                result += length * (length + 1) // 2
                l = r
                r += 1
            if r == len(nums):
                length = r - l
                sums = 0
                for i in range(1, length + 1):
                    sums += i
                result += sums
                l = r
                r += 1
        return result

s = Solution()
print(s.countAlternatingSubarrays([1,0,1,0]))