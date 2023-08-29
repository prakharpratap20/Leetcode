"""
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # if x is 0 or 1 the square root is the number itself, so return x
        if x == 0 or x == 1:
            return x
            
        left, right = 1, x // 2

        # perform binary search until the left boundary is less than or equal to the right boundary 
        while left <= right:
            # calculate the midpoint of the current search range 
            mid = (left + right) // 2

            # calculate the square of the midpoint 
            square = mid * mid

            # if the square of the midpoint is euqal to x, we have found the square root return it
            if square == x:
                return mid
            # if the square of the mid point is less than x, update the left boundary and return it 
            elif square < x:
                left = mid + 1
            # if the square of the midpoint is greater than x, update the right boundary to mid - 1
            else:
                right = mid  - 1

        # if we reach here, it means the binary search didn't find an exact square root, so return the nearest integer (right)
        return right   


