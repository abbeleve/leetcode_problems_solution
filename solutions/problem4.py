class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res_nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res_nums.append(nums1[i])
                i += 1
            else:
                res_nums.append(nums2[j])
                j += 1
        if i == len(nums1) and j < len(nums2):
            res_nums.extend(nums2[j:])
        if j == len(nums2) and i < len(nums1):
            res_nums.extend(nums1[i:])
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (res_nums[(len(nums1) + len(nums2)) // 2 - 1] + res_nums[(len(nums1) + len(nums2)) // 2]) / 2
        else:
            return res_nums[((len(nums1) + len(nums2)) // 2)]

s = Solution()
print(s.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))