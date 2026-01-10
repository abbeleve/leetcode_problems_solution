class Solution:
    def jump(self, nums: list[int]) -> int:
        jump_count = 0
        for index in range(len(nums) - 2, -1, -1):
            jump_range = nums[index]
            if jump_range > 1:
                for long_jump_range in range(jump_range, 0, -1):
                    if index + long_jump_range > len(nums) - 1:
                        continue
                    if nums[index + long_jump_range] == 0:
                        continue
                    jump_count -= long_jump_range + 1
                    break
            elif jump_range == 1:
                jump_count += 1
            else:
                continue
        return jump_count
    
s = Solution()
print(s.jump([2,3,1,1,4]))