class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        unique_nums = list(hash_map.keys())
        while unique_nums:
            first_elem = unique_nums[0]
            amount_of_picked_element = 1
            while amount_of_picked_element < k:
                

s = Solution()
print(s.isPossibleDivide(nums = [1,1,1,2,2,2,2,2,2,3,3,3,4,4,4], k = 3))