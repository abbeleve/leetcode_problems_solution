class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        if nums is None or len(nums) <= 1:
            return 0
        sparsed_counter = [0] * (max(nums) + 1)
        for num in nums:
            sparsed_counter[num] += 1
        res = 0
        for index, num in enumerate(sparsed_counter):
            if num > 1:
                diff = num - 1
                sparsed_counter[index] -= diff
                if index + 1 >= len(sparsed_counter):
                    sparsed_counter.append(diff)
                else:
                    sparsed_counter[index + 1] += diff
                res += diff
        return res

s = Solution()
print(s.minIncrementForUnique([1,0]))