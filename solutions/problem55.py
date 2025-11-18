class Solution:
    def canJump(self, nums: list[int]) -> bool:
        indexes_of_zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                indexes_of_zeros.append(i)
        
        if len(nums) <= 1:
            return True
        
        if nums[0] == 0:
            return False
        
        for zero_indexes in indexes_of_zeros:
            possible_ways = False
            for previous_steps in range(zero_indexes - 1, -1, -1):
                if nums[previous_steps] > zero_indexes - previous_steps:
                    possible_ways = True
                    break
                elif nums[previous_steps] == zero_indexes - previous_steps and zero_indexes == len(nums) - 1:
                    possible_ways = True
                    break
            if not(possible_ways):
                return False
                    
        return True
    
nums = [2,0,0]
s = Solution()
print(s.canJump(nums))