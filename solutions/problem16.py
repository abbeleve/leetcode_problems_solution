class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = 10**9
        for left_border in range(0, len(nums) - 2):
            left_index = left_border + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                summ = nums[left_border] + nums[left_index] + nums[right_index]
                if abs(closest - target) > abs(summ - target):
                    closest = summ
                if summ > target:
                    right_index -= 1
                elif summ < target:
                    left_index += 1
                else:
                    return target

        return closest
    
s = Solution()
print(s.threeSumClosest(nums = [-1,2,1,-4], target = 1))