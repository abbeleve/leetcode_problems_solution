class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        for index, num in enumerate(arr):
            if x < num:
                continue
            elif x == num:
                x_index = index
                break
            else:
                arr.insert(index - 1, x)
                x_index = index - 1
                break
        left_index, right_index = x_index - 1, x_index + 1
        while left_index >= 0 and right_index < len(arr):
            if left_index >= 0:
                arr[left_index] = 