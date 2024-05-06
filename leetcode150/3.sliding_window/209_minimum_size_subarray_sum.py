"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray
whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
"""


class Solution:
    def minSubArrayLen(self, nums, target):
        left, total = 0, 0
        res = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if res == float('inf') else res


if __name__ == '__main__':
    print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
