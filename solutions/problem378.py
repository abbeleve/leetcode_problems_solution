class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        self.matrix = matrix
        height, width = len(matrix), len(matrix[0])
        elems = []
        stack = [[0, 0]]
        while len(stack) > 0:
            minimal_elem_index = stack[0]
            minimal_elem_index_in_stack = 0
            for index, elem in enumerate(stack):
                if matrix[elem[0]][elem[1]] < matrix[minimal_elem_index[0]][minimal_elem_index[1]]:
                    minimal_elem_index = elem
                    minimal_elem_index_in_stack = index
            elems.append(minimal_elem_index)
            elem_index = minimal_elem_index
            if elem_index[1] < width - 1:
                shifted_element = [elem_index[0], elem_index[1] + 1]
                if shifted_element not in stack and shifted_element not in elems:
                    stack.append(shifted_element)
            if elem_index[0] < height - 1:
                shifted_element = [elem_index[0] + 1, elem_index[1]]
                if shifted_element not in stack and shifted_element not in elems:
                    stack.append(shifted_element)
            stack.pop(minimal_elem_index_in_stack)
        return matrix[elems[k - 1][0]][elems[k - 1][1]]
    
s = Solution()
print(s.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))