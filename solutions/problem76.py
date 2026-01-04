class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = {}
        amount_of_letters = {}
        for string in t:
            if string not in hash_map:
                hash_map[string] = []
                amount_of_letters[string] = 1
            else:
                hash_map[string] 
                amount_of_letters[string] += 1

        for index, string in enumerate(s):
            if string in hash_map:
                hash_map[string].append(index)

        

s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))