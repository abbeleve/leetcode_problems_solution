class Solution:
    def queryString(self, s: str, n: int) -> bool:
        MAX_SUBSTRING_LENGTH = 30
        for max_substring_length_ in range(1, 32):
            if 2**max_substring_length_ - 1 >= n:
                MAX_SUBSTRING_LENGTH = max_substring_length_
                break
        set_of_numbers = set()
        for starting_index in range(len(s) - MAX_SUBSTRING_LENGTH + 1):
            substring = s[starting_index:starting_index + MAX_SUBSTRING_LENGTH]
            for subsubstring_length in range(1, MAX_SUBSTRING_LENGTH + 1):
                for subsubstring_starting_index in range(0, len(substring) - subsubstring_length + 1):
                    subsubstring = substring[subsubstring_starting_index:subsubstring_starting_index + subsubstring_length]
                    int_subsubstring = int(subsubstring, 2)
                    if int_subsubstring > n:
                        continue
                    set_of_numbers.add(int_subsubstring)
        set_of_numbers.discard(0)
        return len(set_of_numbers) == n

s = Solution()
print(s.queryString(s = "111100", n = 4))