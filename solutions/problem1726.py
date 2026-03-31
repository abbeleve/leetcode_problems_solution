class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        if len(nums) < 4:
            return 0
        hash_map = {}
        amount_of_combinations = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                hash_map[nums[i] * nums[j]] = hash_map.get(nums[i] * nums[j], 0) + 1
        print(hash_map)
        keys = list(hash_map.keys())
        for product in keys:
            amount_of_products = hash_map[product]
            amount_of_combinations += amount_of_products * (amount_of_products - 1) // 2 * 8
        return amount_of_combinations

s = Solution()
print(s.tupleSameProduct(nums = [1,2,4,5,10]))