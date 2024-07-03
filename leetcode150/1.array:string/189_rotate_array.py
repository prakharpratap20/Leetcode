def rotate(nums, k):
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    Do not return anything, modify nums in-place.
    """
    k = k % len(nums)

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


num = [1, 2, 3, 4, 5, 6, 7, 8]
rotate(num, 4)
print(num)
