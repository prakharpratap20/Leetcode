# class Solution:
#     def rob(self, nums):
#         rob1, rob2 = 0, 0

#         # [rob1, rob2, n, n+1, ...]
#         for n in nums:
#             temp  = max(n+rob1, rob2)
#             rob1 = rob2
#             rob2 = temp
#         return rob2


def rob(nums):
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


nums = [1, 4, 3, 4, 10, 200]

print(rob(nums))
