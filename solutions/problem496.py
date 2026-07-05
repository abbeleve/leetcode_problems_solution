class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash_map = {}
        for index, num in enumerate(nums2):
            hash_map[num] = index
        res = []
        print(hash_map)
        for index in range(len(nums1)):
            res.append(-1)
            num = nums1[index]
            
            index_to_search = hash_map[num]
            print(index_to_search)
            for index_2 in range(index_to_search + 1, len(nums2)):
                if nums2[index_2] > num:
                    res[index] = nums2[index_2]
                    break
        return res

s = Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,2,3,4]))