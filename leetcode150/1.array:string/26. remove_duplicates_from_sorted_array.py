"""Given an integer array nums sorted in non-decreasing order, remove
the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return 
the number of unique element in nums."""

def removeDuplicates(nums) -> int:
    if not nums:
        return 0

    # two pointer approach
    slow, fast = 0, 1

    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    return slow + 1

print(removeDuplicates([1, 2, 2, 2, 3, 4, 4, 5]))
