class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left_pointer = 0
        right_pointer = -1
        result_left_pointer = 0
        result_right_pointer = 10**5
        num_of_letters = {letter:t.count(letter) for letter in t}
        first_time_flag = False

        while right_pointer < len(s) - 1:
            moving_right = False
            for letter in t:
                if num_of_letters[letter] > 0:
                    if s[left_pointer] in num_of_letters and num_of_letters[s[left_pointer]] == 0:
                        moving_right = True
                    else:
                        first_time_flag = True
                        break
            if moving_right:
                right_pointer += 1
                if s[right_pointer] in num_of_letters:
                    num_of_letters[s[right_pointer]] -= 1
            else:
                if s[left_pointer] in num_of_letters:
                    num_of_letters[s[left_pointer]] += 1
                left_pointer += 1
                if first_time_flag:
                    if result_right_pointer - result_left_pointer < right_pointer - left_pointer:
                        result_right_pointer = right_pointer
                        result_left_pointer = left_pointer
        while left_pointer < right_pointer:
            if s[left_pointer] in num_of_letters:
                if num_of_letters[s[left_pointer]] == 0:
                    break
                num_of_letters[s[left_pointer]] += 1
            left_pointer += 1
        for letter in t:
            if num_of_letters[letter] > 0:
                return ""
        return s[left_pointer:right_pointer + 1]

s = Solution()
print(s.minWindow(s = "ab", t = "a"))