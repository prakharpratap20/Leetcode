"""
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are 
not equal to val. Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are 
not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
    
# Example 1:
# Input: nums = [3, 2, 2, 3], val = 3
# After removing all occurrences of 3, nums becomes [2, 2]
# The length of the modified list is 2
solution = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
length1 = solution.removeElement(nums1, val1)
print(f"Example 1: Modified nums1: {nums1[:length1]}, Length: {length1}")

# Example 2:
# Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# After removing all occurrences of 2, nums becomes [0, 1, 3, 0, 4]
# The length of the modified list is 5
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
length2 = solution.removeElement(nums2, val2)
print(f"Example 2: Modified nums2: {nums2[:length2]}, Length: {length2}")

# Example 3:
# Input: nums = [1, 2, 3, 4, 5], val = 6
# Since there are no occurrences of 6, nums remains unchanged
# The length of the modified list is 5
nums3 = [1, 2, 3, 4, 5]
val3 = 6
length3 = solution.removeElement(nums3, val3)
print(f"Example 3: Modified nums3: {nums3[:length3]}, Length: {length3}")
