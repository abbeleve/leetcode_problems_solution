class Solution:
    def swap(self, nums: list[int], first_index: int, last_index: int):
        save = nums[first_index]
        nums[first_index] = nums[last_index]
        nums[last_index] = save

    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        index = 0
        last_index = len(nums) - 1
        while index <= last_index:
            if nums[index] == val:
                self.swap(nums, index, last_index)
                last_index -= 1
                k += 1
            else:
                index += 1
                k += 1
        return index
    
nums = [3,2,2,3]
s = Solution()
res = s.removeElement(nums, 2)
print(res, nums)