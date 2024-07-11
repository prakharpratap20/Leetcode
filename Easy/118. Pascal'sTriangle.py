"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def generate(self, numRows):
        if numRows <= 0:
            return []

        triangle = [[1]]  # initializing the triangle with the first row

        while len(triangle) < numRows:
            prev_row = triangle[-1]  # get the previous row
            new_row = [1]

            for i in range(1, len(prev_row)):
                new_element = prev_row[i-1] + prev_row[i]
                new_row.append(new_element)

            new_row.append(1)  # the last element of each row is always 1
            triangle.append(new_row)

        return triangle

