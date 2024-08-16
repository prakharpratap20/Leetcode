"""
1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution,and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        hash_table = {}

       # Iterate through the 'nums' list
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists in the 'hash_table'
            if complement in hash_table:
                # Return the indices of the current 'num' and the complement
                return [hash_table[complement], i]

            # Add the current 'num' and its index to the 'hash_table'
            hash_table[num] = i

        # Return None if no two numbers satisfy the condition
        return None
