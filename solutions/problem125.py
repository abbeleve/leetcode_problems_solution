import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"\W", "", s)
        s = s.lower()
        s = s.replace('_', '')
        if s == s[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama_'))