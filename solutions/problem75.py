class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            elif i == 2:
                blue += 1
        for i in range(len(nums)):
            if red > 0:
                nums[i] = 0
                red -= 1
            elif white > 0:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2
        return nums
    
s = Solution()
print(s.sortColors(nums = [2,0,2,1,1,0]))