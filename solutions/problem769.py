class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        l = 0
        amount_Of_chunks = 1
        for r in range(1, len(arr)):
            if max(arr[l:r]) == r - 1:
                amount_Of_chunks += 1
                l = r
        return amount_Of_chunks

s = Solution()
print(s.maxChunksToSorted(arr = [2,3,4,1,5,0,6,7]))