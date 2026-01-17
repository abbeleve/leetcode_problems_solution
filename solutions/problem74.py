class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            return self.binarySearch(matrix[0], target)
        for i in range(len(matrix) - 1):
            if matrix[i][0] <= target and matrix[i + 1][0] > target:
                return self.binarySearch(matrix[i], target)
        return self.binarySearch(matrix[-1], target)

    def binarySearch(self, array: list, target: int) -> bool:
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            if array[mid] < target:
                left = mid + 1
                continue
            if array[mid] > target:
                right = mid - 1
                continue
        return False