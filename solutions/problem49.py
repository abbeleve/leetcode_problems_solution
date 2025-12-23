class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map = {}
        groupped_list = []
        index = 0
        for string in strs:
            sorted_tuple_string = tuple(sorted(tuple(string)))
            if sorted_tuple_string not in hash_map:
                hash_map[sorted_tuple_string] = index
                groupped_list.append([string])
                index += 1
            else:
                groupped_list[hash_map[sorted_tuple_string]].append(string)
            
        return groupped_list
    
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
