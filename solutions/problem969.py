class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        result = []
        length = len(arr)
        for i in range(length, -1, -1):
            for j in range(i):
                if arr[j] == i:
                    if j == 0:
                        result.append(i)
                        arr.reverse()
                        
                    else:
                        result.append(j + 1)
                        new_arr = arr[0:j + 1]
                        new_arr.reverse()
                        new_arr.extend(arr[j + 1:])
                        result.append(i)
                        arr = new_arr
                        arr.reverse()
                    break
            arr = arr[:i - 1]
        return result
    
s = Solution()
print(s.pancakeSort(arr = [3,2,4,1]))