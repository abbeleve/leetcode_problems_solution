class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        return " ".join(s.split()[::-1])
        

s = Solution()
print(s.reverseWords("  hello world  "))