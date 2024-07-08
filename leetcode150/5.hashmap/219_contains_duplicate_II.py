"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict = {}

        for i, num in enumerate(nums):
            if num in dict and abs(i - dict[num]) <= k:
                return True
            dict[num] = i

        return False


# Test cases
sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
print(sol.containsNearbyDuplicate([1, 2, 3, 4, 5, 6], 2))  # False
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
