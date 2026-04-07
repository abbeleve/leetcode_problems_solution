import heapq

class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        nums = list(set(nums))
        heapq.heapify(nums)
        while k > 0:
            smallest = nums[0]
            amount_of_smallest = hash_map[smallest]
            if k >= amount_of_smallest:
                hash_map[smallest] -= amount_of_smallest
                heapq.heappop(nums)
                if smallest + 1 not in hash_map:
                    heapq.heappush(nums, smallest + 1)
                hash_map[smallest + 1] = hash_map.get(smallest + 1, 0) + amount_of_smallest
                k -= amount_of_smallest
            else:
                hash_map[smallest] -= k
                if smallest + 1 not in hash_map:
                    heapq.heappush(nums, smallest + 1)
                hash_map[smallest + 1] = hash_map.get(smallest + 1, 0) + k
                k -= k
        num = 1
        for i in nums:
            num *= i ** hash_map[i]
        return num % (10**9 + 7)

s = Solution()
print(s.maximumProduct(nums = [6,4,5,7,8,4,5], k = 4))