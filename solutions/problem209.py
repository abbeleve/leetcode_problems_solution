class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        first_index = 0
        last_index = 1
        minimal_length = 10**4
        sums = sum(nums[first_index:last_index])
        while last_index < len(nums):
            if sums < target:
                sums += nums[last_index]
                last_index += 1
            else:
                minimal_length = min(minimal_length, last_index - first_index)
                if sums + nums[first_index] >= target:
                    sums -= nums[first_index]
                    first_index += 1
                else:
                    sums += nums[last_index]
                    last_index += 1
        while sums >= target:
            minimal_length = min(minimal_length, last_index - first_index)
            sums -= nums[first_index]
            first_index += 1
            sums
        if minimal_length == 10**4:
            return 0
        return minimal_length

s = Solution()
print(s.minSubArrayLen(10, [1,4,4]))