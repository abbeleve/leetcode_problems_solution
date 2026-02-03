class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrom = [0, 1]
        for palindrome_length in range(2, len(s) + 1):
            for i in range(0, len(s) - palindrome_length + 1):
                if self.checkIfPalindrome(s[i:i+palindrome_length]):
                    palindrom = [i, i+palindrome_length]
                    break
        return s[palindrom[0]:palindrom[1]]

    def checkIfPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
s = Solution()
print(s.longestPalindrome(s = "bb"))