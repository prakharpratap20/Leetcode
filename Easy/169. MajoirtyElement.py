"""
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums):
        result, count = 0, 0

        # loop through the elements in the "nums" list
        for n in nums:
            # if the count is zero, assign the current number "n" to result
            if count == 0:
                result = n
            # if the current number "n" is equal to "result", increment the count
            count += (1 if n == result else -1)
        # return the majority element
        return result
