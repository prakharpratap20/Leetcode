"""
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you 
have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix):
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save the topLeft
                topLeft = matrix[top][left+i]

                # move the bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move the bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move the top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move the topLeft back to topRight
                matrix[top + i][right] = topLeft

            right -= 1
            left += 1


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    print(matrix)
    s.rotate(matrix)
    print(matrix)
