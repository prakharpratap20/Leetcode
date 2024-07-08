"""
Given an unsorted array of integers nums, return the length of
the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)

        return max_len


# Test cases
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
print(sol.longestConsecutive([0, 1, 2, 3, 4, 5, 6]))  # 7
print(sol.longestConsecutive([1, 2, 0, 4, 3, 6, 5]))  # 7
print(sol.longestConsecutive([9, 1, 4, 7, 3, 2, 10, 5]))  # 5
print(sol.longestConsecutive([]))  # 0
