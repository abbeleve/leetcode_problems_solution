class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        new_code = []
        if k == 0:
            return [0 for _ in range(len(code))]
        elif k > 0:
            left_index, right_index = 1, 1 + k
            for i in range(len(code)):
                left_index, right_index = (i + 1) % len(code), (i + 1 + k) % len(code)
                if right_index <= left_index:
                    sums = sum(code[0:right_index]) + sum(code[left_index:])
                else:
                    sums = sum(code[left_index:right_index])
                new_code.append(sums)
        else:
            for i in range(len(code)):
                left_index, right_index = i + k, i
                if left_index < 0:
                    left_index = len(code) + left_index
                if right_index < 0:
                    right_index = len(code) + right_index
                if right_index <= left_index:
                    sums = sum(code[0:right_index]) + sum(code[left_index:])
                else:
                    sums = sum(code[left_index:right_index])
                new_code.append(sums)
        return new_code
        
s = Solution()
print(s.decrypt(code = [2,4,9,3], k = -2))