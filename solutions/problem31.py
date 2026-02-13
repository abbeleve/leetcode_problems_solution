import itertools

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums, reverse=True) == nums:
            nums.sort()
            return nums
        for index in range(len(nums) - 2, -1, -1):
            indice = nums[index:]
            permutations = itertools.permutations(sorted(indice))
            perm_list = []
            for perm in permutations:
                perm = list(perm)
                if perm > indice:
                    for i in range(index, len(nums)):
                        nums[i] = perm[i - index]
                    return nums

s = Solution()
print(s.nextPermutation(nums = [1,3,2]))