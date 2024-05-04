"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""


class Solution:
    def candy(self, ratings):
        arr = [1] * len(ratings)

        # first pass (left to right)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        # second pass (right to left)
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j + 1] < ratings[j]:
                arr[j] = max(arr[j], arr[j + 1] + 1)

        return sum(arr)


if __name__ == "__main__":
    print(Solution().candy([1, 0, 2]))
