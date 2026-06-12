class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # t = t[::-1]
        max_palindrome = 1
        max_palindrome = max(max_palindrome, self.findPalindrom(s, t))
        max_palindrome = max(max_palindrome, self.checkForPalindrome(s))
        max_palindrome = max(max_palindrome, self.checkForPalindrome(t))
        return max_palindrome
    
    def checkForPalindrome(self, string):
        for substring_length in range(len(string), 0, -1):
            for i in range(len(string) - substring_length + 1):
                substring = string[i:i+substring_length]
                if self.is_palindrome(substring):
                    return substring_length

    def findPalindrom(self, s: str, t: str) -> int:
        # Идем от самых длинных подстрок к коротким
        for substring_length in range(len(s), 0, -1):
            for i in range(len(s) - substring_length + 1):
                s_substring = s[i:i+substring_length]
                
                # Разворачиваем подстроку из s, чтобы искать её зеркальное отражение в t
                reversed_substring = s_substring[::-1]
                
                if reversed_substring in t:
                    found_index = t.index(reversed_substring)
                    
                    # Проверяем, можно ли расширить палиндром на 1 символ в центре
                    # Вариант А: в s есть символ справа от подстроки
                    has_center_in_s = (i + substring_length < len(s))
                    
                    # Вариант Б: в t есть символ "между" (так как подстрока перевернута, 
                    # символ слева от нее в t окажется внутри палиндрома при склейке s + t)
                    has_center_in_t = (found_index > 0)
                    
                    if has_center_in_s or has_center_in_t:
                        return substring_length * 2 + 1
                    else:
                        return substring_length * 2
                        
        return 0

    def is_palindrome(self, text):
        return text == text[::-1]

s = Solution()
print(s.longestPalindrome(s = "vn", t = "ln"))