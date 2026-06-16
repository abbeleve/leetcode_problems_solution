import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        left_saved = left + 0
        right_saved = right + 0
        right = math.ceil(math.sqrt(right))
        left = 1
        generated_palindrome_odd = int(str(left) + str(left)[:-1][::-1])
        generated_palindrome_even = int(str(left) + str(left)[::-1])
        counter = 0
        while generated_palindrome_odd < right or generated_palindrome_even < right:
            if self.is_palindrome(generated_palindrome_odd ** 2) and generated_palindrome_odd ** 2 < right_saved and generated_palindrome_odd ** 2 >= left_saved:
                counter += 1
            if self.is_palindrome(generated_palindrome_even ** 2) and generated_palindrome_even ** 2 < right_saved and generated_palindrome_even ** 2 >= left_saved:
                counter += 1
            left += 1
            generated_palindrome_odd = int(str(left) + str(left)[:-1][::-1])
            generated_palindrome_even = int(str(left) + str(left)[::-1])

        return counter

    def is_palindrome(self, number: int):
        return str(number) == str(number)[::-1]

s = Solution()
print(s.superpalindromesInRange("40000000000000000", "50000000000000000"))