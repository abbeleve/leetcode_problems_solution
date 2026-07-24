from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        monotonic_stack = deque()
        set_of_letters = set()
        for i in s:
            set_of_letters.add(i)
        amount_of_letters = len(list(set_of_letters))
        hash_map = {}
        for index, letter in enumerate(s):
            while monotonic_stack and letter < monotonic_stack[-1]:
                monotonic_stack.pop()
            monotonic_stack.append(letter)
            hash_map[letter] = index
            if amount_of_letters == len(list(hash_map.keys())):
                break
        res = "".join(sorted(list(hash_map.keys()), key=lambda x: hash_map[x]))
        return res
    
s = Solution()
print(s.removeDuplicateLetters(s = "cbacdcbc"))