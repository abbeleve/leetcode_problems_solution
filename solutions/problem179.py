class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        max_number = max(nums)
        max_length = len(str(max_number))
        hash_map = {}
        for index in range(len(nums)):
            num = nums[index]
            nums[index] = str(nums[index]) + (max_length - len(str(nums[index]))) * ':'
            hash_map[nums[index]] = num
        nums.sort(reverse=True)
        print(nums)
        for index in range(len(nums)):
            nums[index] = nums[index].replace(':', '')
        return "".join(nums)
    
s = Solution()
print(s.largestNumber([3,30,34,5,9]))