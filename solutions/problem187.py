class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        left_pointer, right_pointer = 0, 10
        result = []
        hash_map = {}
        word = None
        while right_pointer < len(s) + 1:
            if word is None:
                word = s[left_pointer:right_pointer]
            else:
                word = word[1:] + s[right_pointer - 1]
            if word not in hash_map:
                hash_map[word] = 1
            elif hash_map[word] == 1:
                result.append(word)
                hash_map[word] += 1
            right_pointer += 1
            left_pointer += 1
        return result
    
s = Solution()
print(s.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))