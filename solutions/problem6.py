class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        additional_amount_of_symbols = numRows - 2
        partition_length = numRows + additional_amount_of_symbols
        s += (partition_length - (len(s) % partition_length)) * " "
        newS = []
        for part_index in range(0, len(s), partition_length):
            newS.append(s[part_index:part_index+partition_length])
        left_index, right_index = 0, len(newS[0]) - 1
        resulting_string = ""
        while left_index <= right_index:
            only_left_index = True
            for i in range(len(newS)):
                part_newS = newS[i]
                if left_index == 0 or left_index == numRows - 1:
                    resulting_string += part_newS[left_index]
                    only_left_index = True
                    continue
                resulting_string += part_newS[left_index] + part_newS[right_index]
                only_left_index = False
            if only_left_index:
                left_index += 1
            else:
                left_index += 1
                right_index -= 1
        return resulting_string.replace(" ", "")


s = Solution()
print(s.convert("ABC", 2))