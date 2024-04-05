"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""


def majorityElement(nums):
    # boyer-moore voting algo
    result, count = None, 0

    for num in nums:
        if count == 0:
            result = num
        if num == result:
            count += 1
        else:
            count -= 1

    return result


print(majorityElement([1, 1, 2, 2, 2, 1, 1]))
