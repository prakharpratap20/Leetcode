"""
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    # calculate prefix product
    prefix_product = 1
    for i in range(n):
        output[i] = prefix_product
        prefix_product = prefix_product * nums[i]

    # calculate suffic product
    suffix_product = 1
    for i in range(n-1, -1, -1):
        output[i] = output[i] * suffix_product
        suffix_product = suffix_product * nums[i]

    return output


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
