class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first_pointer = 0
        last_pointer = 1
        substring = s[first_pointer:last_pointer]
        max_length_of_substring = 1
        while last_pointer < len(s):
            indexofelem = substring.find(s[last_pointer])
            if indexofelem != -1:
                first_pointer = indexofelem + 1
                substring = s[first_pointer:last_pointer]
            else:
                substring += s[last_pointer]
                max_length_of_substring = max(max_length_of_substring, len(substring))
            last_pointer += 1
        if len(s) == 0:
            return 0
        return max_length_of_substring

s = Solution()
print(s.lengthOfLongestSubstring("aab"))