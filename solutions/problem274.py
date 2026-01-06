class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        index = 0
        while index < len(citations) - 1:
            if citations[index] != citations[index + 1] or index == len(citations) - 2:
                amount_of_papers = index + 1
                h_index = citations[index]
                if amount_of_papers >= h_index:
                    return amount_of_papers
            index += 1
        if len(citations) <= citations[-1]:
            return len(citations)
        return len(citations)
                
s = Solution()
print(s.hIndex([1,3,1]))