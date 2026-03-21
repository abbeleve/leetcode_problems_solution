class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        x_index = 0
        for index, num in enumerate(arr):
            if num < x:
                x_index = index + 1
            elif x == num:
                x_index = index
                break
            else:
                x_index = index
                break
        result = []
        left_index, right_index = x_index - 1, x_index
        while (left_index >= 0 or right_index < len(arr)) and (k > 0):
            if left_index >= 0 and right_index < len(arr):
                left_abs = x - arr[left_index]
                right_abs = arr[right_index] - x
                if left_abs <= right_abs:
                    result.append(arr[left_index])
                    left_index -= 1
                elif left_abs > right_abs:
                    result.append(arr[right_index])
                    right_index += 1
            elif left_index >= 0:
                result.append(arr[left_index])
                left_index -= 1
            elif right_index < len(arr):
                result.append(arr[right_index])
                right_index += 1
            k -= 1
        return sorted(result)
    
s = Solution()
print(s.findClosestElements(arr = [1], k = 1, x = 0))