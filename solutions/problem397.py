class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1 :
            return 0
        stack = [n]
        hash_map = {n: 0}
        while len(stack) > 0:
            num = stack.pop()
            if num & 1 == 0:
                new_num = num >> 1
                if new_num in hash_map:
                    hash_map[new_num] = min(hash_map[new_num], hash_map[num] + 1)
                else:
                    hash_map[new_num] = hash_map[num] + 1
                stack.append(new_num)
                if new_num == 1:
                    stack.pop()
            else:
                stack.append(num + 1)
                hash_map[num + 1] = hash_map[num] + 1
                stack.append(num - 1)
                hash_map[num - 1] = hash_map[num] + 1
                if num - 1 == 1:
                    stack.pop()
        return hash_map[1]

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n & 1 == 0:
                n = n // 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            count += 1
        return

s = Solution()
print(s.integerReplacement(65535))