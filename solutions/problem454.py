class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        possible_numbers = {}
        for num_1 in nums3:
            for num_2 in nums4:
                possible_numbers[num_1 + num_2] = possible_numbers.get(num_1 + num_2, 0) + 1
        res = 0
        for num_1 in nums1:
            for num_2 in nums2:
                number = num_1 + num_2
                if -1*number in possible_numbers:
                    res += possible_numbers[-1*number]
        return res

s = Solution()
print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))