"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""


class Solution:
    def threeSum(self, nums):
        triplets = []
        nums.sort()  # sort the input array in non decreasing order

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate value of nums[i]

            left, right = i + 1, len(nums) - 1  # two pointer approach

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # skip duplicate values of nums[left] and nums[right]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets

