class Solution:
    def convert(self, s: str, numRows: int) -> str:
        elem_in_split = 2 * numRows - 2
        elem_to_add_to_s = elem_in_split - (len(s) % elem_in_split)
        s += " "*elem_to_add_to_s
        arr = []
        for i in range(0, len(s), elem_in_split):
            arr.append(s[i:i+elem_in_split])
        print(arr)
        result_string = ""
        for i in range(elem_in_split):
            for string in arr:
                result_string += string[i]
        print(result_string)

        result_string = result_string.strip()
        return result_string
        

s = Solution()
print(s.convert("PAYPALISHIRING", 3))