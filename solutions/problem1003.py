class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        while i < len(s) - 2:
            if s[i:i+3] == "abc":
                s = s[:i] + s[i+3:]
                i = max(i - 2, 0)
            else:
                i += 1
        return len(s) == 0