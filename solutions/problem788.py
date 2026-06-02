class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_digits = [0, 1, 2, 5, 6, 8, 9]
        changing_digits = {2, 5, 6, 9}

        candidates = [1, 2, 5, 6, 8, 9]
        count = 0

        i = 0
        while i < len(candidates):
            num = candidates[i]
            i += 1

            if num > n:
                break

            s = str(num)
            has_change = any(int(d) in changing_digits for d in s)

            if has_change:
                count += 1
            
            for d in good_digits:
                new_num = num * 10 + d
                if new_num <= n:
                    candidates.append(new_num)
                else:
                    break

        return count

s = Solution()
print(s.rotatedDigits(10))