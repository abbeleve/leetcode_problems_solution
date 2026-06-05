class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)

        if min_val == max_val:
            return 0

        bucket_size = (max_val - min_val) / (len(nums) - 1)
        bucket_count = int((max_val - min_val) // bucket_size + 1)
        buckets = [[None, None] for _ in range(bucket_count)]
        for num in nums:
            idx = int((num - min_val) // bucket_size)
            if buckets[idx][0] is None:
                buckets[idx][0] = num
                buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        max_gap = 0
        prev_max = min_val

        for bucket_min, bucket_max in buckets:
            if bucket_min is None:
                continue
            max_gap = max(max_gap, bucket_min - prev_max)
            prev_max = bucket_max

        return max_gap

s = Solution()
print(s.maximumGap(nums = [1,3,100]))