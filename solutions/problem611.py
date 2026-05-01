class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        self.nums = sorted(nums)
        amount_of_combinations = 0
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums) - 1):
                first_number, second_number = self.nums[i], self.nums[j]
                bigger_numbers_index = self.binarySearch(j + 1, first_number + second_number)
                amount_of_combinations += bigger_numbers_index - j - 1
        return amount_of_combinations

    def binarySearch(self, left_index, target):
        right_index = len(self.nums) - 1
        while left_index <= right_index:
            mid = (left_index + right_index) // 2
            if self.nums[mid] > target:
                right_index = mid - 1
            elif self.nums[mid] < target:
                left_index = mid + 1
            else:
                while mid - 1 >= left_index and self.nums[mid - 1] == target:
                    mid -= 1
                return mid
        return left_index
    
s = Solution()
print(s.triangleNumber(nums = [0,0,0]))