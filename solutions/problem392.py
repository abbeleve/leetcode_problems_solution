class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s = 0
        index_t = 0
        while index_s < len(s) and index_t < len(t):
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            else:
                index_t += 1
        if index_s == len(s):
            return True
        if index_t == len(t):
            return False

s = Solution()
print(s.isSubsequence('abc', 'ahbgdc'))