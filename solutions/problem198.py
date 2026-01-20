class Solution:
    def rob(self, nums: list[int]) -> int:
        payload = []
        for index, num in enumerate(nums):
            if len(payload) < 2:
                payload.append(num)
                continue
            print(payload)
            payload.append(max(payload[0:len(payload) - 1]) + num)
        return max(payload)
    
s = Solution()
print(s.rob([2,7,9,3,1]))