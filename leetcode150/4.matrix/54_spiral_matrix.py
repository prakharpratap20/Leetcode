"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""


class Solution:
    def spiralOrder(self, matrix):
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every j in the right column
            for j in range(top, bottom):
                res.append(matrix[j][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every j in the left column
            for j in range(bottom - 1, top - 1, -1):
                res.append(matrix[j][left])
            left += 1

        return res


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(matrix))
