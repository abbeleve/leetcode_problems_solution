class Solution:
    def hIndex(self, citations: list[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)
        unique_numbers = set(sorted_citations)
        index = 0
        while index < len(sorted_citations) and sorted_citations[index] >= len(sorted_citations):
            index += 1

        hypot_h = None
        while index < len(sorted_citations):
            if index != 0:
                past_hypot_h = sorted_citations[index - 1]
            else:
                past_hypot_h = sorted_citations[index]
            hypot_h = sorted_citations[index]
            print(sorted_citations[index:])
            if sorted_citations[index] == 0:
                break

            while index < len(sorted_citations) and sorted_citations[index] == hypot_h:
                index += 1
            
            if index >= hypot_h:
                print(index, hypot_h)
                correct_hypot = hypot_h
                for hypot in range(hypot_h + 1, past_hypot_h):
                    if hypot > index - 1:
                        return hypot - 1
                return hypot_h

            
            #index += 1
        
        for hypot in range(sorted_citations[index - 1], 0, -1):
            print(hypot)
            if index >= hypot:
                return hypot

        return 0
    
s = Solution()
print(s.hIndex([1,7,9,4]))