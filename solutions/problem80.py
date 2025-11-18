class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        saved_index = 0
        duplicates = 0
        i = 0
        k = 0
        length = len(nums)
        while i < length:
            if nums[i] == nums[saved_index]:
                duplicates += 1

            if nums[i] != nums[saved_index]:
                if duplicates > 2:
                    saved_index += 2
                    left_swap_index = saved_index
                    for right_swap_index in range(i, length):
                        # self.swap(nums, left_swap_index, right_swap_index)
                        nums[left_swap_index] = nums[right_swap_index]
                        left_swap_index += 1
                    i = saved_index
                    k += 2
                    length -= (duplicates - 2) 
                    duplicates = 0
                else:
                    saved_index += duplicates
                    k += duplicates
                    duplicates = 0
                
                continue
            i += 1
        
        if duplicates > 2:
            duplicates = 2
        k += duplicates
        return k
    
    def swap(self, nums, i, j):
        save = nums[i]
        nums[i] = nums[j]
        nums[j] = save


nums = [1, 1, 1]
s = Solution()
print(s.removeDuplicates(nums))
print(nums)