import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-1*i for i in nums]
        heapq.heapify(nums)
        print(nums)
        if k == 1:
            return -nums[0]
        for i in range(k):
            res = heapq.heappop(nums)
        return -1*res
    
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))