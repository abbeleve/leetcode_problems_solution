class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr_n = [int(i) for i in str(n)]
        flag = False
        for i in range(len(arr_n) - 2, -1, -1):
            if arr_n[i] >= arr_n[i + 1]:
                continue
            flag = True
            break
        if not(flag):
            return -1
        min_j = arr_n[i] + 1
        best_j = 10
        index_j = len(arr_n) - 1
        for j in range(len(arr_n) - 1, i, -1):
            if arr_n[j] < best_j and arr_n[j] >= min_j:
                best_j = arr_n[j]
                index_j = j
        arr_n[i], arr_n[index_j] = arr_n[index_j], arr_n[i]
        right_part = arr_n[i + 1:]
        if len(right_part) == 1:
            res = 0
            for index, num in enumerate(reversed(arr_n)):
                res += num * (10 ** index)
            return res if res <= 2147483647 else -1
        right_part.sort()
        res = 0
        for index, num in enumerate(reversed(right_part)):
            res += num * (10 ** index)
        for index, num in enumerate(reversed(arr_n[:i + 1])):
            res += num * (10 ** (index + len(right_part)))
        return res if res <= 2147483647 else -1

s = Solution()
print(s.nextGreaterElement(2147483647))