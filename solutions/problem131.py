from functools import lru_cache

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.combinations = []
        self.s = s
        self.process([], s)
        return self.combinations

    def process(self, combination: list, left_string: str):
        if len(left_string) == 0:
            self.combinations.append(combination[:])
            return

        for index in range(1,len(left_string) + 1):
            substring = left_string[0:index]
            if self.is_palindrome(substring):
                combination.append(substring)
                self.process(combination=combination, left_string=left_string[index:])
                combination.pop()

    @lru_cache
    def is_palindrome(self, s: str) -> bool:
        offset = 1 if len(s) % 2 == 0 else 0
        if s[0:len(s) // 2] == s[len(s) - 1:len(s) // 2 - offset:-1]:
            return True
        return False
    
s = Solution()
print(s.partition(s="a"))