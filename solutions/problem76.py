class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = {}
        amount_of_letters = {}
        for string in t:
            if string not in hash_map:
                hash_map[string] = []
                amount_of_letters[string] = 1
            else:
                # hash_map[string]
                amount_of_letters[string] += 1

        for index, string in enumerate(s):
            if string in hash_map:
                hash_map[string].append(index)

        left_index = len(s)
        right_index = 0        
        for string in t:
            left_index = min(left_index, hash_map[string][0])
            right_index = max(right_index, hash_map[string][0])
        # CREATING BEST APPROACH SO LEFT INDEX IS MOST LEFT AND RIGHT INDEX IS MOST LEFT TOO

        while right_index < len(s) - 1:
            while True:
                

s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))