class Solution:
    def rob(self, nums: list[int]) -> int:
        payload = []
        max_payload_index_odd = 0
        max_payload_index_even = 0
        for num in nums:
            payload.append()