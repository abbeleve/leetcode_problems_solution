class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        if len(nums) == 0:
            return result
        if len(nums) == 1:
            return [str(nums[0])]
        starting_number = nums[0]
        ending_number = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1] - 1:
                if starting_number == ending_number:
                    result.append(str(starting_number))
                else:
                    result.append(f"{starting_number}->{ending_number}")
                starting_number = nums[i + 1]
                ending_number = nums[i + 1]
                if i + 1 == len(nums) - 1:
                    result.append(str(nums[i + 1]))
            else:
                ending_number = nums[i + 1]
                if i + 1 == len(nums) - 1:
                    result.append(f"{starting_number}->{nums[i + 1]}")
        return result

s = Solution()
print(s.summaryRanges([0,1]))