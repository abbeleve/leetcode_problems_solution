class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left, right = 0, 0
        prefix_product = 1
        res = 0
        if k <= 1:
            return 0
        nums.append(k)
        while right < len(nums):
            prefix_product = prefix_product * nums[right]
            if prefix_product < k:
                right += 1
            else:
                while prefix_product >= k and left <= right:
                    prefix_product = prefix_product // nums[left]
                    left += 1
                    res += right - left + 1
                right += 1

        return res
