class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s == goal:
                return True
            s = s[-1] + s[:-1]
        return False

s = Solution()
print(s.rotateString(s = "abcde", goal = "cdeab"))