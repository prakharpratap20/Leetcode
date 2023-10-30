"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # merge the array into a single sorted list 
        merged = nums1 + nums2

        # sort the merged array
        merged.sort()

        # calculate the total number of elements in the merged array
        total = len(merged)

        if total % 2 == 1: #odd
            return float(merged[total//2])
        else:
            middle1 = merged[total//2 - 1]
            middle2 = merged[total//2]
            return (float(middle1) + float(middle2)) / 2.0