"""
1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store numbers encountered and their indices
        hash_table = {}
        
        # Loop through 'nums' list to find two numbers whose sum equals 'target'
        for i, num in enumerate(nums):
            # Calculate the complement, which is the difference between 'target' and the current 'num'
            complement = target - num
            
            # Check if the complement exists in the 'hash_table'
            if complement in hash_table:
                # Return the indices of the current 'num' and the complement
                return [hash_table[complement], i]
            
            # Add the current 'num' and its index to the 'hash_table'
            hash_table[num] = i
        
        # Return None if no two numbers satisfy the condition
        return None






