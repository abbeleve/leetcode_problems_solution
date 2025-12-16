class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        word_length = len(needle)
        word_ending_index = word_length - 1
        while word_ending_index < len(haystack):
            if haystack[word_ending_index] == needle[-1]:
                for 