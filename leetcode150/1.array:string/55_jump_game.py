"""You are given an integer array nums. You are initially positioned at the array's
first index and each element in the array represents your maximum jump length at that
position.
Return true if you can reach the last index or false otherwise."""

def can_jump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i+nums[i])

    return max_reach >= len(nums)
