class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        total = len(merged)
        if total % 2 == 1:
            return merged[total // 2]
        else:
            mid_right = total // 2
            mid_left = mid_right - 1
            return (merged[mid_left] + merged[mid_right]) / 2