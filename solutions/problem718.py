class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        hash_set = set()
        for max_length in range(1, len(nums2) + 1):
            for left_index in range(len(nums2) - max_length + 1):
                string = tuple(nums2[left_index:left_index+max_length])
                hash_set.add(string)
        for max_length in range(len(nums1), 0, -1):
            for left_index in range(len(nums1) - max_length + 1):
                string = tuple(nums1[left_index:left_index+max_length])
                if string in hash_set:
                    return max_length
        return 0
    
s = Solution()
print(s.findLength([70,39,25,40,7], [52,20,67,5,31]))