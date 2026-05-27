class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        if intervals is None:
            return
        index_hash_map = {}
        for index, interval in enumerate(intervals):
            interval_start = interval[0] # since its unique
            index_hash_map[interval_start] = index
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        sorted_starts = [i[0] for i in sorted_intervals]
        hash_map = {}
        for index, interval in enumerate(sorted_intervals):
            interval_start = interval[0]
            hash_map[index] = index_hash_map[interval_start]
        result = [-1] * len(intervals)
        for index, i in enumerate(intervals):
            found_index = self.binarySearch(i[1], sorted_starts)
            if found_index < len(intervals):
                result[index] = hash_map[found_index]
        return result

    def binarySearch(self, elem, arr):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if elem < arr[m]:
                r = m - 1
            elif elem > arr[m]:
                l = m + 1
            else:
                return m
        return l
        

s = Solution()
print(s.findRightInterval(intervals = [[1,4],[2,3],[3,4]]))