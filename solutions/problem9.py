class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left_part = x[:len(x)//2]
        right_part = x[(len(x)//2 + len(x)%2):]
        return left_part == right_part[::-1]

s = Solution()
print(s.isPalindrome(131))