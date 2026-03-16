class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hash_map = {}
        result = []
        amount_of_nums = len(nums)
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
            if hash_map[num] > int(amount_of_nums / 3):
                result.append(num)
                hash_map[num] = -100000
        return result
