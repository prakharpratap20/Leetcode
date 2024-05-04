"""
Given n non-negative integers representing an elevation map where the width 
of each bar is 1, compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height):
        n = len(height)

        if n <= 2:
            return 0

        left = [0] * n
        right = [0] * n

        left[0], right[n-1] = height[0], height[n-1]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        for j in range(n-2, -1, -1):
            right[j] = max(right[j + 1], height[j])

        trapped_water = 0

        for i in range(n):
            trapped_water += min(left[i], right[i]) - height[i]

        return trapped_water


if __name__ == "__main__":
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
