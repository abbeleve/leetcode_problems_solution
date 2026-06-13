class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # t = t[::-1]
        max_palindrome = 1
        max_palindrome = max(max_palindrome, self.findPalindrom(s, t))
        max_palindrome = max(max_palindrome, self.checkForPalindrome(s))
        max_palindrome = max(max_palindrome, self.checkForPalindrome(t))
        return max_palindrome
    
    def checkForPalindrome(self, string):
        for substring_length in range(len(string), 0, -1):
            for i in range(len(string) - substring_length + 1):
                substring = string[i:i+substring_length]
                if self.is_palindrome(substring):
                    return substring_length

    def findPalindrom(self, s, t):
        for substring_length in range(len(s), 0, -1):
            for i in range(len(s) - substring_length + 1):
                s_substring = s[i:i+substring_length]
                print(s_substring)
                try:
                    found_index = t.index(s_substring[::-1])
                    print(found_index)
                    # print(i + substring_length)
                    if found_index != 0:
                        return substring_length * 2 + 1
                    if i + substring_length != len(s):
                        return substring_length * 2 + 1
                    return substring_length * 2
                except:
                    pass
        return 1

    def is_palindrome(self, text):
        return text == text[::-1]

s = Solution()
print(s.longestPalindrome(s = "vn", t = "ln"))