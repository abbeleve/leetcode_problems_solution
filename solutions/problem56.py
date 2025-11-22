class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged_result = []
        li = 0
        if len(intervals) == 0:
            return intervals
        while True:
            amount_of_mergings = 0
            while li < len(intervals) - 1:
                intervals[li], intervals[li + 1] = self.sort_two_items(intervals[li]), self.sort_two_items(intervals[li + 1])
                if (intervals[li][1] >= intervals[li + 1][0] and intervals[li][0] <= intervals[li + 1][1]) or (intervals[li][0] <= intervals[li + 1][1] and intervals[li][1] >= intervals[li + 1][0]):
                    merged_result.append([min(intervals[li][0], intervals[li+1][0]), max(intervals[li][1], intervals[li + 1][1])])
                    li += 1
                    amount_of_mergings += 1
                else:
                    merged_result.append(intervals[li])
                    if li + 1 == len(intervals) - 1:
                        merged_result.append(intervals[li + 1])
                li += 1
            if amount_of_mergings == 0:
                return merged_result
            intervals = merged_result
            print(intervals)
    
    def sort_two_items(self, li):
        if li[0] > li[1]:
            return [li[1], li[0]]
        return [li[0], li[1]]
    
s = Solution()
print(s.merge([[1,4],[0,2],[3,5]]))