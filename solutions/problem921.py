class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        res = 0
        for bracket in s:
            if bracket == "(":
                if balance > 0:
                    res += balance
                    balance = 0
                balance -= 1
            else:
                balance += 1
        res += abs(balance)
        return res

s = Solution()
print(s.minAddToMakeValid("())"))