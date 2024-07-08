"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# Test cases
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1] (2 + 7 = 9)
print(sol.twoSum([3, 2, 4], 6))  # [1, 2] (2 + 4 = 6)
print(sol.twoSum([3, 3], 6))  # [0, 1] (3 + 3 = 6)
print(sol.twoSum([-1, -2, -3, -4, -5], -8))  # [2, 4] (-3 + -5 = -8)
