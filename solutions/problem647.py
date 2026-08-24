class Solution:
    def countSubstrings(self, s: str) -> int:
        l, r = 0, 2
        amount = len(s)
        while r < len(s):
            if self.is_palindrome(s[l:r]):
                amount += 1
            

    def is_palindrome(self, s):
        return s == s[::-1]